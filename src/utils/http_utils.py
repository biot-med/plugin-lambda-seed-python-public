import json

import requests

from src.constants import TRACEPARENT_KEY, default_headers, API_CALL_ERROR
from src.utils.configure_logger import logger


def create_headers(traceparent=None, token=None, additional_header_dict=None):
    headers = default_headers.copy()

    if traceparent is not None:
        headers.update({TRACEPARENT_KEY: traceparent})

    if token is not None:
        headers.update({"Authorization": "Bearer " + token})

    if additional_header_dict is not None:
        headers.update(additional_header_dict)

    return headers


def post(url, traceparent=None, token=None, body=None, query_params=None, headers=None) -> dict:
    """ This method simplifies post request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('POST', url, traceparent, token, body, query_params, headers)


def biot_search(url, query_params, traceparent=None, token=None, body=None, headers=None) -> dict:
    """ This method simplifies the bioT standard search request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         query_params (dict): The query params of the request. This will be wrapped in searchRequest key.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return get(url, traceparent, token, body, {"searchRequest": query_params}, headers)


def get(url, traceparent=None, token=None, body=None, query_params=None, headers=None) -> dict:
    """ This method simplifies get request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('GET', url, traceparent, token, body, query_params, headers)


def options(url, traceparent=None, token=None, body=None, query_params=None, headers=None):
    """ This method simplifies options request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('OPTIONS', url, traceparent, token, body, query_params, headers)


def head(url, traceparent=None, token=None, body=None, query_params=None, headers=None):
    """ This method simplifies head request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('HEAD', url, traceparent, token, body, query_params, headers)


def put(url, traceparent=None, token=None, body=None, query_params=None, headers=None) -> dict:
    """ This method simplifies put request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('PUT', url, traceparent, token, body, query_params, headers)


def patch(url, traceparent=None, token=None, body=None, query_params=None, headers=None) -> dict:
    """ This method simplifies patch request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """
    return _request('PATCH', url, traceparent, token, body, query_params, headers)


def delete(url, traceparent=None, token=None, body=None, query_params=None, headers=None):
    """ This method simplifies delete request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     """
    _request('DELETE', url, traceparent, token, body, query_params, headers)


def _request(method, url, traceparent=None, token=None, body=None, query_params=None, headers=None):
    """ This method simplifies request APIs.
        Any API call that does not respond with a 2XX success code will throw in an exception.
        It will add the default headers, token and traceparent to the request headers.

     Args:
         method (string): The method of the request, may be one of the following: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
         url (string): The url of the API.
         traceparent (string): The traceparent, optional.
         token (string): JWT for the authorization header, optional.
         body (dict): The json body of the request, optional.
         query_params (dict): The query params of the request, optional.
         headers (dict): The headers of the request, optional.

     Returns:
         dict: response.
     """

    logger.info("Sending http request: ", {"method": method, "url": url, "query_params": query_params,
                                           "body": body, "headers": headers})

    if query_params is not None:
        for key, value in query_params.items():
            if value is not None and isinstance(value, dict):
                query_params[key] = json.dumps(value)

    try:
        response = requests.request(
            method=method,
            url=url,
            headers=create_headers(traceparent, token, headers),
            json=body,
            params=query_params
        )

        log_response(response)

        if response.status_code == 204:
            return {}

        return response.json()

    except Exception as exception:
        raise Exception(API_CALL_ERROR, {"cause": exception})


def log_response(response, response_body_log_override=None):
    if response is None:
        raise Exception("No response returned")
    else:
        if response_body_log_override is None:
            logger.info("Received http response: ", {"status code": response.status_code,
                                                     "body": response.text,
                                                     "headers": response.headers})
        else:
            logger.info("Received http response: ", {"status code": response.status_code,
                                                     "body": response_body_log_override,
                                                     "headers": response.headers})

    if response.status_code not in range(200, 299):
        raise Exception("Response returned with non 2XX status code: " + response.text)
