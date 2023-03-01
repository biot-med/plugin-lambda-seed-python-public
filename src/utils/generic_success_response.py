def generic_success_response (traceId):
    return {
        "statusCode": 200,
        "headers": {
            "x-b3-traceid": traceId,
        }
    }