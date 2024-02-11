# README

# BioT's general lambda seed.

_This is a basic template for lambda to be used as a starting point for AWS lambdas extending BioT's services._

[Read here](https://docs.biot-med.com/docs/biot-plugins) about BioT plugins. 

This seed works with different triggers (i.e hook type - either notification or interceptors).
Each hooktype has to be managed in a specific way and has different functions accordingly (both to manage the event and for the return value).
The lambda first determines what hook is used and retrieves the relevant functions (using a mapper).
For the lambda to work as is, the hooktype property must be specified in the header sent in the event (except for non-specific lambdas).

## Setup

First we create the virtual environment - Run in command line (use *python/python3* depends on the installation)
```
python3 -m venv seedenv
```
then activate (on Mac)
```
source seedenv/bin/activate
```
(windows)
```
./seedenv/Scripts/activate
```
then run (while the virtual machine is activated) to install all the relevant dependencies 
```
pip install -r requirements.txt 
```

**IMPORTANT** If you add a new dependency while working (pip install), make sure to add the dependency to the requirements.txt file by running  
```
pip freeze > requirements.txt 
```
### Start working

#### Hello world - hooktype Notification example

after setting up 

Go To [src/notification/perform.py](./src/notification/perform.py) 

Add this code in the designated place 
```
    logger.info("Hello World")
```

run to create plugin.zip file
```
python3 scripts/pack.py
```

Upload the the plugin.zip as with notification subscription to any action for any entity as explained [here](https://docs.biot-med.com/docs/custom-lambda-deployment#plugin-api-call)

Now go and perform the action you subscribed to 

In plugin configurations page (Console app) - preview - you have a link to the aws console. open it and go to monitoring (tab) -> View CloudWatch logs (button)

In the logs you can see the lambda ran and specifically the "Hello world" record 

_You can read the comments and TODOs specified in the code to further understand the functions and flow._

### Maintenance Notes
1. The pack script has some assumptions:
  - The handler function is in the index.py (its zipped specifically) 
  - Some dependencies directories are NOT zipped - 
    - "pip", 'pkg_resources', 'setuptools', '_distutils_hack', 'distutils-precedence.pth' that are added automatically when creating the venv
    - all folders with '.dist-info' suffix
2. Whenever a change is being made, make sure to update the version in the \_\_version\_\_.py file

### Cleaning up unwanted code

If you are using the lambda seed for just one hook type, you can remove all folders not relevant for the usage and delete the `check_request_type` and the `functions_mapper` lines, then import the functions normally (with import) directly from the remaining folder. For instance, for interceptorPre, use:

`from src.interceptor_pre.index import authenticate, login, extractDataFromEvent, perform, createErrorResponse`

Unused steps and functions can be removed as well.

### Constants

For running locally you can use local_dev_constants in the constants file.
Just make sure to fill the variables according to the lambda's variables **in the dev environment**

## Supported hooks

- Notifications - notification services
  - hooktype name: `NOTIFICATION`
- Interceptors for pre-requests
  - hooktype name: `INTERCEPTOR_PRE`
- Interceptors for post-requests
  - hooktype name: `INTERCEPTOR_POST`
- Interceptors for Adapt entity (which are also post-requests)
  - hooktype name: `INTERCEPTOR_POST_ENTITY`
- Other general lambda types not mentioned above
  - ( hooktype not required but in the code accessed using `NONSPECIFIC` )

## Basic code flow

**This is the lambda's basic flow (see the root index.js file):**

1. These basic functions run at the beginning of the lambda (you can change them as required):

- `check_request_type(event)` - this function checks the hook type from the event. If the lambda has only one usage this can be removed (along with the following functionsMapper).

- `functions_mapper[request_type]` - This contains the functions from the relevant hook type folder. If you use the lambda for just one of the hooks you can import the functions directly from the folder and delete this line.

- `extract_data_from_event` - extract the data, metadata, traceparent and token from the lambda's event (this is diffract for each hook type).

- `traceparent = event_traceparent if event_traceparent is not None else create_traceparent()` - get a traceparent from the event (or fallback to a traceparent from a BioT service)

- `configure_logger` - creating new logs format that follows the structure required for dataDog logs (including a traceId). Environment variable BIOT_SHOULD_VALIDATE_JWT should be false if the lambda does not receive a token, otherwise authentication will fail the lambda

- `authenticate` - authenticate the token sent by the notification service.

- `login` - login the lambda (service user) and get a token

- `perform` - This is where you write your code. The `perform` functions typically call `call_to_api_example` to show an example of calling a BioT service. The interceptors also show an example of changing the data sent in the request/response.
  Note: Not all the argument set to the perform function are relevant for every hook type, so fallbacks are supplied to prevent code errors.
  _Make sure to remove the examples in the lambda and substitute your own._

- `create_error_response` - This is a mapper for errors to be returned from the lambda.
  - In case of interceptors, the data structure is important (follow the data structure supplied for the interceptors in their `create_error_response` function).
  - If you add a new error code, add the error's code name to the constants, add the error response in `create_error_response`, and use `raise Exception(ERROR_CODE_NAME)` where the error occur in your code.

## Environment variables

**Make sure to define these env variables in your lambda**:

- `BIOT_APP_NAME` - name of this lambda - this is for logging purposes

- `BIOT_BASE_URL` - for example https://api.int.biot-med.com

- `BIOT_JWT_PERMISSION_INTERCEPTION` or `BIOT_JWT_PERMISSION_NOTIFICATION` - permissions sent in the token.
  The default for this is a single string - `ACTION_NOTIFICATION` for notifications or `PLUGIN_INTERCEPTOR` for interceptors.

- `BIOT_SERVICE_ENVIRONMENT` - for instance "gen2int"

- `BIOT_SERVICE_USER_ID` - the lambdas service users id

- `BIOT_SERVICE_USER_SECRET_KEY` - the lambdas service users secret key

- `BIOT_SHOULD_VALIDATE_JWT` - This should be false if the service does not
