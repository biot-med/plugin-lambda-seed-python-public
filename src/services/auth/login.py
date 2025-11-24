import time
from calendar import timegm
from datetime import datetime

import requests

from src.utils.configure_logger import logger
from src.constants import (
    BIOT_BASE_URL,
    BIOT_SERVICE_USER_ID,
    BIOT_SERVICE_USER_SECRET_KEY,
    TRACEPARENT_KEY,
)

# Cache for access token to avoid logging in on every invocation
# These module-level variables persist across invocations within the same Lambda container
_access_token_cache = None
_access_token_expiration = None
# Refresh token 1 minute before expiration to avoid edge cases
_TOKEN_REFRESH_BUFFER_SECONDS = 60


def _is_cached_token_valid():
    """Checks if the cached access token is still valid (not expired and not about to expire).

    Returns:
        bool: True if the cached token is valid, False otherwise.
    """
    global _access_token_cache, _access_token_expiration

    if _access_token_cache is None or _access_token_expiration is None:
        return False

    current_time = time.time()
    # Check if token is still valid (with buffer to refresh before expiration)
    return current_time < (_access_token_expiration - _TOKEN_REFRESH_BUFFER_SECONDS)


def _cache_token(access_token, expiration_str):
    """Caches the access token and its expiration time.

    Args:
        access_token (string): The access token to cache.
        expiration_str (string): The expiration time in ISO 8601 format (e.g., "2025-11-24T09:23:14.945Z").
    """
    global _access_token_cache, _access_token_expiration

    # Parse ISO 8601 datetime string (format: "2025-11-24T09:23:14.945Z")
    # The 'Z' indicates UTC, so we can parse it as UTC
    # Replace 'Z' with '+00:00' to make it timezone-aware, then convert to naive UTC
    expiration_str_normalized = expiration_str.replace('Z', '+00:00')
    expiration_dt = datetime.fromisoformat(expiration_str_normalized)
    # Convert to naive UTC datetime (remove timezone info since it's already UTC)
    expiration_dt_naive = expiration_dt.replace(tzinfo=None)
    expiration_timestamp = timegm(expiration_dt_naive.utctimetuple())
    
    # Update cache
    _access_token_cache = access_token
    _access_token_expiration = expiration_timestamp


def login(traceparent):
    """Logs the service user into the BioT system and returns an access token.
    
    The access token is cached and reused across invocations within the same Lambda container.
    A new token is fetched only when the cached token is expired or about to expire.

    Args:
        traceparent (string): traceparent.

    Returns:
        string: The access token to be used by subsequent requests to the BioT API.
    """
    global _access_token_cache, _access_token_expiration

    # Check if we have a cached token that's still valid
    if _is_cached_token_valid():
        logger.info("ben test - Using cached access token")
        return _access_token_cache

    logger.info("ben test - Fetching new access token")
    # Cache miss, expired, or about to expire - fetch new token
    if BIOT_BASE_URL is None:
        raise Exception("No BIOT_BASE_URL")
    if BIOT_SERVICE_USER_ID is None:
        raise Exception("No BIOT_SERVICE_USER_ID")
    if BIOT_SERVICE_USER_SECRET_KEY is None:
        raise Exception("No BIOT_SERVICE_USER_SECRET_KEY")

    url = BIOT_BASE_URL + "/ums/v2/services/accessToken"
    res = requests.post(
        url,
        json={
            "id": BIOT_SERVICE_USER_ID,
            "secretKey": BIOT_SERVICE_USER_SECRET_KEY,
        },
        headers={
            TRACEPARENT_KEY: traceparent,
        }
    )

    response_data = res.json()
    access_token = response_data["accessToken"]
    expiration_str = response_data["accessTokenExpiration"]
    
    # Cache the token and its expiration time
    _cache_token(access_token, expiration_str)

    return access_token

