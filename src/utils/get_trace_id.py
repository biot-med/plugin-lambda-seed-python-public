import requests
from constants import BIOT_BASE_URL
from configure_logger import logger
# This is a fallback to get a traceId for this lambdas uses only.
# If it does not exist, it fallbacks to get a traceId from an existing BioT API using it's healthCheck API


API_TO_GET_TRACE_ID_FROM = f"{BIOT_BASE_URL}/ums/system/healthCheck"

def get_trace_id():
    """Get a trace id using BioT's healthCheck service.

    Returns:
        string: trace_id
    """

    #This tries to get the response from an existing BioT service (using it's healthCheck)
    res_trace_id = None
    try:
        res = requests.get(API_TO_GET_TRACE_ID_FROM)
        res_trace_id = res.json()["traceId"]
    except:
        logger.error("Error getting new trace id, setting to default")
    finally:
        if res_trace_id is not None:
            return res_trace_id
        else:
            return "traceId_Missing"