import requests
from src.constants import API_CALL_ERROR, BIOT_BASE_URL

def call_api_example(new_token, trace_id):
    """ This get request asks for patients from organization API.

    Args:
        token (string): JWT for the authorization header.
        trace_id (string): The trace id.

    Returns:
        dict: empty dict or list of patients.
    """

    biot_api_call_url = f"{BIOT_BASE_URL}/organization/v1/users/patients"
    try:

        response = requests.get(
            url=biot_api_call_url,
            headers={
                "authorization": "Bearer " + new_token,
                "x-b3-traceid": trace_id
            }
        )

        if response is None or response.status_code != 200:
            raise Exception(API_CALL_ERROR)
        
        patients = response.json()["data"]["patients"] if "data" in response.json() and "patients" in response.json()["data"] else {}
        return patients

    except Exception:
        raise Exception(API_CALL_ERROR)
