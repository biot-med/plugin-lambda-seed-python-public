import requests
from src.constants import BIOT_PUBLIC_KEY, JWT_ERROR, JWT_PERMISSION, BIOT_BASE_URL, BIOT_SERVICE_USER_ID, BIOT_SERVICE_USER_SECRET_KEY, TRACEPARENT_KEY
from datetime import datetime
from calendar import timegm
from jose import jws
from jose.constants import ALGORITHMS
from jose.exceptions import ExpiredSignatureError, JWTClaimsError
from src.utils.configure_logger import logger
import json

def authenticate(token):
    """Autheticate the original JWT by verifying signature and expiration.

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

def login (traceparent):
    """Logs the service user into the BioT system and returns an access token.

    Args:
        traceparent (string): traceparent.

    Returns:
        string: The access token to be used by subsequent requests to the BioT API.
    """

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
            [TRACEPARENT_KEY]: traceparent,
        }
    )

    return res.json()["accessToken"]


def check_jwt (token, required_permission = None):
    try:
        decoded = jws.verify(token, BIOT_PUBLIC_KEY, ALGORITHMS.RS512)
        claims = json.loads(decoded.decode("utf-8"))

        if "exp" not in claims:
            return claims
        try:
            exp = int(claims["exp"])
        except ValueError:
            raise JWTClaimsError("Expiration Time claim (exp) must be an integer.")
        now = timegm(datetime.utcnow().utctimetuple())
        if exp < now:
            raise ExpiredSignatureError("Signature has expired.")
        
        if required_permission is None:
            return
            
        # TODO: If you need to, update this function to add other permissions to be checked in the JWT
      
        # Checks the required permission in the token

        if required_permission not in claims["scopes"]:
            raise Exception(f'JWT does not have the required permissions. Missing: {required_permission}')
    except Exception as e:
        logger.error('Error: ', e)
        raise Exception(JWT_ERROR)