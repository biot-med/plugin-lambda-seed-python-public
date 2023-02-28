def genericSuccessResponse (traceId):
    return {
        "statusCode": 200,
        "headers": {
            "x-b3-traceid": traceId,
        }
    }