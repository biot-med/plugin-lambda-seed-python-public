from src.constants import TRACEPARENT_KEY


def generic_success_response(traceparent):
    return {
        "statusCode": 200,
        "headers": {
            TRACEPARENT_KEY: traceparent,
        }
    }


def generic_success_response_with_body(traceparent, body):
    return {
        "statusCode": 200,
        "headers": {
            TRACEPARENT_KEY: traceparent,
        },
        "body": body
    }


def generic_bad_request_response(traceparent, body):
    return {
        "statusCode": 400,
        "headers": {
            TRACEPARENT_KEY: traceparent,
        },
        "body": body
    }
