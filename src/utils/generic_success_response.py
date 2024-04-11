from src.constants import TRACEPARENT_KEY


def generic_success_response(traceparent):
    return {
        "statusCode": 200,
        "headers": {
            TRACEPARENT_KEY: traceparent,
        }
    }


def generic_success_response_with_body(traceparent, body: dict):
    return {
        "statusCode": 200,
        "headers": {
            TRACEPARENT_KEY: traceparent,
        },
        "body": body
    }

