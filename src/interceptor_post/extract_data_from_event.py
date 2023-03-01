import json
from constants import NO_EVENT_ERROR, NO_DATA_ERROR, JWT_ERROR

def extractDataFromEvent(event): 
    if event is None:
        raise Exception(NO_EVENT_ERROR)
    event_headers = event["headers"]
    parsed_event_body = json.loads(event["body"])
    
    event_with_parsed_data = event
    event_with_parsed_data["body"] = parsed_event_body

    data = event_with_parsed_data
    event_token = event_headers["authorization"].split(" ")[1]
    event_trace_id = event_headers["x-b3-traceid"]

    if data is None:
        raise Exception(NO_DATA_ERROR)
    if event_token is None:
        raise Exception(JWT_ERROR)

    return {
        "data": data,
        "event_token": event_token,
        "event_trace_id": event_trace_id,
    }
