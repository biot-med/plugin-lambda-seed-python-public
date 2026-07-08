# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A seed/template repository for a BioT AWS Lambda plugin, written in Python. It's meant to be forked/cloned by
plugin authors as a starting point, then trimmed down to whichever "hook type" they actually need. There are no
automated tests in this repo — verification is done by running `local_runner.py` or deploying and checking
CloudWatch logs.

## Commands

Local dev setup (only needed for `local_runner.py`, not for packing):
```
python3 -m venv seedenv
./seedenv/Scripts/activate      # windows
source seedenv/bin/activate     # mac/linux
pip install -r requirements.txt
```
If you add a dependency during local dev, refresh the lockfile: `pip freeze > requirements.txt`.

Run a mock invocation locally (uses `mock_event.py`, no AWS needed):
```
python local_runner.py
```
Swap which mock event is used by editing the import in [local_runner.py](local_runner.py) (`notification_mock_event`,
`pre_intercept_mock_event`, or `nonspecific_mock_event` from `mock_event.py`).

Build the deployable ZIP plugin:
```
python scripts/pack.py
```
This installs Linux-targeted wheels (`manylinux2014_x86_64` by default) straight into `package/` via
`pip install --platform ... --target package`, copies `src/` and `index.py` in, and zips it to `plugin.zip`.
It does **not** use the local venv, and the host Python does not need to match the Lambda runtime — pip resolves
wheels for the target. For arm64 Lambdas, change `LAMBDA_PLATFORM` in [scripts/pack.py](scripts/pack.py) to
`manylinux2014_aarch64`. To target a different Lambda Python runtime, change `TARGET_PY`.

Docker image deployment (alternative to ZIP): scripts under `scripts/docker/{linux,windows}/` handle
login/build/push/run/destroy against the BioT plugin docker repository. See [README.md](README.md) for the full
credential/deploy sequence — it's a multi-step manual process (get temp credentials → login script → buildAndPush →
call Plugin API with the image tag).

CI (Jenkins, see [Jenkinsfile](Jenkinsfile)): runs `scripts/pack.py`, reads the version from `__version__.py`,
skips upload if that version's zip already exists in the `biot-plugin-seed` S3 bucket, otherwise uploads
`seed_py_<version>.zip` and tags the commit on `master`.

**Whenever you change code here, bump `__version__` in [__version__.py](__version__.py)** — and update the
`User-Agent` version string in `default_headers` in [src/constants.py](src/constants.py) to match. Also add an
entry to [CHANGELOG.md](CHANGELOG.md).

## Architecture

### Hook types and dispatch

The lambda handles multiple "hook types" (BioT plugin trigger kinds), each with its own folder under `src/`:

- `src/notification/` — `NOTIFICATION` — fired on BioT actions/events.
- `src/interceptor_pre/` — `INTERCEPTOR_PRE` — runs before a request; can rewrite the outgoing request.
- `src/interceptor_post/` — `INTERCEPTOR_POST` — runs after a request.
- `src/interceptor_post_entity/` — `INTERCEPTOR_POST_ENTITY` — post-request interceptor specific to "Adapt entity".
- `src/nonspecific/` — `NONSPECIFIC` — fallback for any other lambda usage; used when no `hooktype` header is
  present or it doesn't match a known type.

Each folder exposes the same four-function contract via its `index.py`: `extract_data_from_event`, `perform`,
`create_error_response`, plus re-exported `authenticate`/`login` from `src/services/auth/`. `src/index.py` builds
`functions_mapper`, a dict from hook-type string to that folder's module. [index.py](index.py) (root) is the actual
Lambda entrypoint (`handler`) and is the only file the pack script zips specifically as the handler.

`src/utils/check_request_type.py` reads the `hooktype` header (case-insensitively) off the incoming event and
selects which folder's functions run. **If a plugin only ever needs one hook type**, the intended cleanup (per
README) is: delete the other hook-type folders, delete `check_request_type`/`functions_mapper`, and import that
one folder's four functions directly in `index.py`.

### Request flow (index.py `handler`)

1. `check_request_type(event)` → picks the hook-type module from `functions_mapper`.
2. `extract_data_from_event(event)` → hook-type-specific parsing of `data`/`event_token`/`event_traceparent`
   (and `metadata` for notifications) out of the raw event. Parsing differs meaningfully per hook type (e.g.
   `interceptor_pre` unescapes double-escaped JSON in the body; `notification` requires `metadata`/`data`/`jwt`
   keys to be present or raises).
3. Traceparent resolution: use the one from the event, else `create_traceparent()` (in
   `src/utils/traceparent_utils.py`) generates a fallback w3c-format traceparent.
4. `logger.configure_logger(traceparent)` — sets a class-level trace ID on the custom `logger` class so all
   subsequent structured logs (DataDog-compatible JSON lines) carry it.
5. `authenticate(event_token)` — only called if `BIOT_SHOULD_VALIDATE_JWT` is true. Validates the JWT against
   BioT's public key (fetched once per container and cached at module scope in
   `src/services/auth/authenticate.py`) and checks it has `JWT_PERMISSION` (from constants/env) among its scopes.
6. `login(traceparent)` — logs in the lambda's own service user (`BIOT_SERVICE_USER_ID`/`SECRET_KEY`) to get an
   access token for calling BioT APIs. The token is cached at module scope in `src/services/auth/login.py` and
   reused across invocations in the same warm container until ~60s before expiry.
7. `perform(data, token, traceparent, metadata)` — **this is where plugin-specific logic goes**; everything else
   in the seed is scaffolding around it. The provided implementation just calls `call_api_example` (in
   `src/utils/call_to_api_example.py`) as a demo and should be replaced.
8. On exception, `create_error_response(e, traceparent)` maps the raised error to a hook-type-specific response
   shape. Error codes are matched against constants in `src/constants.py` (e.g. `NO_DATA_ERROR`, `JWT_ERROR`,
   `ACCESS_DENIED_ERROR`); unmatched errors fall back to a generic internal server error. **To add a new error
   type**: add the constant in `src/constants.py`, add its handling in the relevant `create_error_response.py`,
   and `raise Exception(THE_CONSTANT)` at the point of failure. Note `interceptor_pre`'s `create_error_response`
   matches on `error.args[0]` while other hook types match on the exception itself — follow whichever pattern
   the folder you're editing already uses.

### Config / constants (`src/constants.py`)

Two parallel constant dicts — `cloud_constants` (reads from env vars, used when deployed) and
`local_dev_constants` (hardcoded values for local runs) — selected via `environment_constants` based on whether
`AWS_REGION` is set (i.e., whether it's actually running in AWS). Edit `local_dev_constants` to point at a real
dev environment when using `local_runner.py` against live BioT services. All the module-level constants
(`BIOT_BASE_URL`, `JWT_PERMISSION`, etc.) are derived from `environment_constants` once at import time.

### Shared utilities (`src/utils/`)

- `http_utils.py` — thin wrapper over `requests` (`get`/`post`/`put`/`patch`/`delete`/`options`/`head`/
  `biot_search`) that injects `default_headers`, bearer token, and traceparent; raises on non-2xx; logs request
  and response. Prefer this over calling `requests` directly for calls to BioT APIs.
- `configure_logger.py` — the `logger` class; structured JSON logs shaped for DataDog (`@timestamp`, `level`,
  `traceId`, `appName`, ...). Use `logger.info/warn/error/debug` instead of `print`.
- `traceparent_utils.py` — w3c traceparent creation/parsing (trace ID is the second dash-delimited segment).
- `file.py` — upload/download link generation and file transfer helpers against BioT's file service.
- `call_to_api_example.py` — example calls against BioT APIs; meant to be deleted/replaced by real plugin logic,
  not extended.

### Local vs. deployed entrypoint

`local_runner.py` imports `handler` from the root `index.py` and invokes it directly with a mock event — no Lambda
runtime involved. Docker-based local testing instead runs the actual Lambda Runtime Interface Emulator on
`localhost:9000` inside the container built from [Dockerfile](Dockerfile) (see README's "Local Run Before Deploy").
