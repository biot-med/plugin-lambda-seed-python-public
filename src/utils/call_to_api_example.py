import json

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


def call_api_with_query_param_example(token, traceparent, searchRequest: dict) -> dict:
    """ This get request asks for entities relationships from entity service.

    Args:
        token (string): JWT for the authorization header.
        traceparent (string): The traceparent.
        searchRequest: the search request

    Returns:
        dict: empty dict or list of entities relationships.
    """

    url = f"{BIOT_BASE_URL}/generic-entity/v1/generic-entities"

    search_request_for_query_param = {
        "searchRequest": json.dumps(searchRequest)
    }

    return http_utils.get(url, traceparent, token, body={}, query_params=search_request_for_query_param)


def call_api_with_path_var_example(token, traceparent, id: str) -> dict:
    """ This get request asks for the patient that is related to the provided id.

        Args:
            token (string): JWT for the authorization header.
            traceparent (string): The traceparent.
            id: the id of the entity

        Returns:
            dict: empty dict or the wanted entity.
    """

    url = f"{BIOT_BASE_URL}/organization/v1/users/patients/{id}"
    return http_utils.get(url, traceparent, token)



def call_api_with_special_header_example(token, traceparent, request_body: dict, caregiver_template_name: str):
    """ This POST API creates a caregiver in the system.

    Args:
        token (string): JWT for the authorization header
        traceparent (string): The traceparent.
        request_body (dict): The caregiver to create
        caregiver_template_name (str): name of the caregiver template

        Returns:
             dict: the created caregiver
    """

    url = f"{BIOT_BASE_URL}/organization/v1/users/caregivers/templates/{caregiver_template_name}"
    headers = {
        "Email-Confirmation-Landing-Page": "https://organization.app.dev.biot-gen2.biot-med.com/auth/invitation"
    }

    return http_utils.post(url, traceparent, token, request_body, headers=headers)