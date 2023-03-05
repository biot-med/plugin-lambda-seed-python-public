import json
from src.constants import NO_EVENT_ERROR, NO_METADATA_ERROR, NO_DATA_ERROR, JWT_ERROR

def extract_data_from_event (event):
    if event is None or "body" not in event:
        raise Exception(NO_EVENT_ERROR)

    parsed_event = json.loads(event["body"])

    if "metadata" not in parsed_event or parsed_event["metadata"] is None:
        raise Exception(NO_METADATA_ERROR)
    if "data" not in parsed_event or parsed_event["data"] is None:
        raise Exception(NO_DATA_ERROR)
    if "jwt" not in parsed_event or parsed_event["jwt"] is None:
        raise Exception(JWT_ERROR)

    return {
        "metadata": parsed_event["metadata"],
        "data": parsed_event["data"],
        "event_token": parsed_event["jwt"],
        "event_trace_id": parsed_event["metadata"]["traceId"] if "traceId" in parsed_event["metadata"] else None
    }

