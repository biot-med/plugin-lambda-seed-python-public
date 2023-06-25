import requests
from src.constants import API_CALL_ERROR, BIOT_BASE_URL, TRACEPARENT_KEY

# This is a call to a BioT API, it can be any call provided the lambda service user has permission

def call_api_example(new_token, traceparent):
    """ This get request asks for patients from organization API.

    Args:
        token (string): JWT for the authorization header.
        traceparent (string): The traceparent.

    Returns:
        dict: empty dict or list of patients.
    """

    biot_api_call_url = f"{BIOT_BASE_URL}/organization/v1/users/patients"
    try:

        response = requests.get(
            url=biot_api_call_url,
            headers={
                "authorization": "Bearer " + new_token,
                [TRACEPARENT_KEY]: traceparent
            }
        )

        if response is None or response.status_code != 200:
            raise Exception(API_CALL_ERROR)
        
        patients = response.json()["data"]["patients"] if "data" in response.json() and "patients" in response.json()["data"] else {}
        return patients

    except Exception as e:
        raise Exception(API_CALL_ERROR, {"cause": e})
