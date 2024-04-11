import json
from src.constants import NO_EVENT_ERROR, NO_DATA_ERROR, JWT_ERROR, TRACEPARENT_KEY


def extract_data_from_event(event): 
    if event is None:
        raise Exception(NO_EVENT_ERROR)
    event_headers = event["headers"]
    parsed_event_body = json.loads(event["body"].replace("\\\\", "\\"))

    event_with_parsed_data = event
    event_with_parsed_data["body"] = parsed_event_body

    data = event_with_parsed_data
    event_token = event_headers["authorization"].split(" ")[1] if "authorization" in event_headers else None
    event_traceparent = event_headers[TRACEPARENT_KEY] if TRACEPARENT_KEY in event_headers else None

    if data is None:
        raise Exception(NO_DATA_ERROR)
    if event_token is None:
        raise Exception(JWT_ERROR)

    return {
        "data": data,
        "event_token": event_token,
        "event_traceparent": event_traceparent,
    }
