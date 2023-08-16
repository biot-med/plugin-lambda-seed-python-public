from src.constants import BIOT_BASE_URL
from src.utils import http_utils


# This is a call to a BioT API, it can be any call provided the lambda service user has permission

def call_api_example(token, traceparent):
    """ This get request asks for patients from organization API.

    Args:
        token (string): JWT for the authorization header.
        traceparent (string): The traceparent.

    Returns:
        dict: empty dict or list of patients.
    """

    url = f"{BIOT_BASE_URL}/organization/v1/users/patients"
    return http_utils.get(url, traceparent, token, body={})
