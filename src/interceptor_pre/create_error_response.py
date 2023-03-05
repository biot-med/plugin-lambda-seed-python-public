from src.constants import API_CALL_ERROR, JWT_ERROR, NO_EVENT_ERROR, NO_DATA_ERROR, BIOT_SERVICE_ENVIRONMENT, BIOT_APP_NAME
from src.utils.configure_logger import logger

env_fallback = "Not specified"

def build_response_error(status_code, code, message, trace_id):
    return {
        "statusCode": status_code,
        "body": {
            "code": code,
            "message": message,
            "serviceName": BIOT_APP_NAME if BIOT_APP_NAME is not None else env_fallback,
            "traceId": trace_id,
            "environment": BIOT_SERVICE_ENVIRONMENT if BIOT_SERVICE_ENVIRONMENT is not None else env_fallback,
            "details": {},
        },
    }

def api_error(error, trace_id):
    return build_response_error(
        status_code=500,
        code=API_CALL_ERROR,
        message=f"Call to api failed { f': {error}' if error is not None or error != '' else '.' }",
        trace_id=trace_id
    )

def jwt_error(error, trace_id):
    return build_response_error(
        status_code=400,
        code=JWT_ERROR,
        message=f"JWT error occurred { f': {error}' if error is not None or error != '' else '.' }",
        trace_id=trace_id
    )

def no_event_error(error, trace_id):
    return build_response_error(
        status_code=400,
        code=NO_EVENT_ERROR,
        message="No event sent",
        trace_id=trace_id
    )

def no_data_error(error, trace_id):
    return build_response_error(
        status_code=400,
        code=NO_DATA_ERROR,
        message="no data sent in event",
        trace_id=trace_id
    )

def internal_server_error(error, trace_id):
    return build_response_error(
        status_code=500,
        code="SERVER ERROR",
        message="internal server error",
        trace_id=trace_id
    )

errors = {
    API_CALL_ERROR: api_error,
    JWT_ERROR: jwt_error,
    NO_EVENT_ERROR: no_event_error,
    NO_DATA_ERROR: no_data_error,
    "internalServerError": internal_server_error
}

def create_error_response (error, trace_id):
    logger.error("Got error: ", error)
    if error is not None and error in errors:
        return errors[error](error, trace_id)
    else:
        return errors["internalServerError"](error, trace_id)

