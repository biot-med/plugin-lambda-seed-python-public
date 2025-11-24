import requests
from jose import jwt
from jose.constants import ALGORITHMS
from src.constants import (
    GET_PUBLIC_KEY_API_URL,
    JWT_ERROR,
    JWT_PERMISSION,
    BIOT_BASE_URL,
)

# Cache for public key to avoid fetching it on every invocation
# This module-level variable persists across invocations within the same Lambda container
public_key = None


def construct_public_key(public_key_response):
    """Constructs the public key in PEM format.

    Args:
        public_key_response (string): The raw public key string.

    Returns:
        string: The public key in PEM format.
    """
    return "-----BEGIN PUBLIC KEY-----\n" + public_key_response + "\n-----END PUBLIC KEY-----"


def get_public_key():
    """Gets the public key.

    Returns:
        string: The raw public key string.
    """
    if BIOT_BASE_URL is None:
        raise Exception("No BIOT_BASE_URL")

    url = BIOT_BASE_URL + GET_PUBLIC_KEY_API_URL
    res = requests.get(url)
    return res.json()["publicKey"]


def check_jwt(token, required_permission=None):
    """Validates the JWT token and checks for required permission.

    Args:
        token (string): The JWT token to validate.
        required_permission (string, optional): The required permission to check.
    """
    global public_key

    # Fetch and cache public key if not already cached
    if public_key is None:
        response_public_key = get_public_key()
        public_key = construct_public_key(response_public_key)

    # This validates the token sent by the notification service
    # jwt.decode automatically handles expiration checking (like JWT.verify in Node.js)
    try:
        jwt_data = jwt.decode(token, public_key, algorithms=[ALGORITHMS.RS512])
    except Exception:
        raise Exception(JWT_ERROR)

    if not required_permission:
        return

    # Checks the required permission in the token
    if not jwt_data.get("scopes") or required_permission not in jwt_data["scopes"]:
        raise Exception(f'JWT does not have the required permissions. Missing: {required_permission}')


def authenticate(token):
    """This validates the token sent by the notification service and checks the required permission.

    Args:
        token (string): The original JWT.
    """
    try:
        """ 
        This validates the token sent by the notification service and checks the required permission

        This implementation checks JWT_PERMISSION from constants.py.
        You can define it in your plugin's environment variables, see constants.py
        """
        check_jwt(token, JWT_PERMISSION)
        return
    except Exception as e:
        raise Exception(JWT_ERROR, {"cause": e})

