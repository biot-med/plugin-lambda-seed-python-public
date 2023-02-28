import requests
from constants import BIOT_PUBLIC_KEY, JWT_ERROR, BIOT_JWT_PERMISSION, BIOT_BASE_URL, BIOT_SERVICE_USER_ID, BIOT_SERVICE_USER_SECRET_KEY
from datetime import datetime
from calendar import timegm
from jose import jws
from jose.constants import ALGORITHMS
from jose.exceptions import ExpiredSignatureError, JWTClaimsError
import json

def authenticate(token):
    """Autheticate the original JWT by verifying signature and expiration.

    Args:
        token (string): The original JWT.

    Returns:
        dictionary: The decoded and verified JWT.
    """

    try:
        decoded = jws.verify(token, BIOT_PUBLIC_KEY, ALGORITHMS.RS512)
        claims = json.loads(decoded.decode("utf-8"))
        print("This is the decoded and verified JWT: ", claims)
        print("Verifying JWT expiration.")
        if "exp" not in claims:
            return claims
        try:
            exp = int(claims["exp"])
        except ValueError:
            raise JWTClaimsError("Expiration Time claim (exp) must be an integer.")
        now = timegm(datetime.utcnow().utctimetuple())
        if exp < now:
            raise ExpiredSignatureError("Signature has expired.")
        print("Verified JWT expiration. now: " + str(now) + ". exp: " + str(exp))

        if BIOT_JWT_PERMISSION is not None and BIOT_JWT_PERMISSION not in claims["scopes"]:
            raise(f"JWT does not have the required permissions. Missing: {BIOT_JWT_PERMISSION}")
        
        return claims
    except Exception as e:
        print(e)
        raise Exception(JWT_ERROR)

def login (trace_id):
    """Logs the service user into the BioT system and returns an access token.

    Args:
        trace_id (string): trace_id.

    Returns:
        string: The access token to be used by subsequent requests to the BioT API.
    """

    if BIOT_BASE_URL is None:
        raise Exception("No BIOT_BASE_URL")
    if BIOT_SERVICE_USER_ID is None:
        raise Exception("No BIOT_SERVICE_USER_ID")
    if BIOT_SERVICE_USER_SECRET_KEY is None:
        raise Exception("No BIOT_SERVICE_USER_SECRET_KEY")

    res = requests.post(
        BIOT_BASE_URL + "/ums/v2/services/accessToken",
        json={
            "id": BIOT_SERVICE_USER_ID,
            "secretKey": BIOT_SERVICE_USER_SECRET_KEY,
        },
        headers={
            "x-b3-traceid": trace_id,
        }
    )

    print("Login response: " + json.dumps(res.json()))

    return res.json()["accessToken"]
