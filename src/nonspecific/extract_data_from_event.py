import json
from src.constants import NO_EVENT_ERROR, NO_DATA_ERROR, JWT_ERROR


def extract_data_from_event(event):
    if event is None:
        raise Exception(NO_EVENT_ERROR)

    if event.get("body"):
        body_str: str = event["body"]
        parsed_event = json.loads(body_str.replace("\\n", ""))

        if parsed_event is None:
            raise Exception(NO_DATA_ERROR)

        return parsed_event
    else:
        return {}
