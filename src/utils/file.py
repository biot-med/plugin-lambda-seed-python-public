import requests

from src.constants import BIOT_BASE_URL
from src.utils import http_utils
from src.utils.configure_logger import logger
from src.utils.http_utils import log_response


def generate_upload_link(traceparent, token, file_name, mime_type):
    """Generates a file upload link"""

    return http_utils.post(url=BIOT_BASE_URL + "/file/v1/files/upload",
                           traceparent=traceparent,
                           token=token,
                           body={
                               "name": file_name,
                               "mimeType": mime_type
                           })


def generate_download_link(traceparent, token, file_id):
    """Generates a file download link"""

    return http_utils.get(url=BIOT_BASE_URL + "/file/v1/files/" + file_id + "/download",
                          traceparent=traceparent,
                          token=token)


def upload_file(url, file):
    """Uploads a file to a given url"""

    logger.info("Sending http request: ", {"method": "PUT", "url": url, "query_params": None,
                                           "body": "file", "headers": None})
    response = requests.put(
        url=url,
        data=file
    )
    log_response(response)
    return response


def download_file(url):
    """Downloads a file from a given url"""

    logger.info("Sending http request: ", {"method": "GET", "url": url, "query_params": None,
                                           "body": None, "headers": None})
    response = requests.request(
        method="GET",
        url=url)
    log_response(response, response_body_log_override="file")
    return response.content
