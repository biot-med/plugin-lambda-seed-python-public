import json


def create_pre_intercept_success_response(data: dict):
    return json.dumps({
        "request": {
            "path": data["body"]["request"]["path"],
            "queryParameters": data["body"]["request"]["queryParameters"],
            "headers": data["body"]["request"]["headers"],
            "body": data["body"]["request"]["body"]
        }
    })
