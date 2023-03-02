
import json
from src.index import get_trace_id, logger, check_request_type, functions_mapper, BIOT_SHOULD_VALIDATE_JWT

# This is just an example!
# The structure of the event can be anything

def handler (event):
    # The following two logs are just for debugging. You should remove them as soon as you can, the token should not be printed to logs.
    logger.info("At Lambda start, got event: ", event)
    logger.info("At Lambda start, got body: ", json.loads(event["body"]))

    trace_id = "traceId-not-set"

    # This mapper makes it possible to use all types of the lambdas hooks (notification, interceptors or any other non-specific hooks)
    # This requestType can be replaced with spreading the specific functionsMapper for your type of hook, or a direct import of the types functions
    # Then you can remove checkRequestType and the mapper
    # Example: For interceptorPre, you can remove this and at the top of this file add:
    #          import { authenticate, login, extractDataFromEvent, perform, createErrorResponse } from "./src/interceptorPre/index.js"
    request_type = check_request_type(event)

    authenticate = functions_mapper[request_type].authentiate
    login = functions_mapper[request_type].login
    extract_data_from_event = functions_mapper[request_type].create_error_response
    perform = functions_mapper[request_type].perform
    create_error_response = functions_mapper[request_type].create_error_response

    try:
        # This extracts the data, metadata, token and traceId from the event
        # Note: Some of these properties might not be relevant for certain cases, you can remove them if they are not relevant
        #       For example, metadata does not exist in interceptors' events.
        extracted_data = extract_data_from_event[event]
        data = extracted_data["data"] if "data" in extracted_data else None
        event_token = extracted_data["event_token"] if "event_token" in extracted_data else None
        event_trace_id = extracted_data["event_trace_id"] if "event_trace_id" in extracted_data else None
        metadata = extracted_data["metadata"] if "metadata" in extracted_data else None

        # We extract the traceId from the event
        # As a fallback, if the traceId is not included, we get a new traceId from a open BioT AIP service
        trace_id = event_trace_id if event_trace_id is not None else get_trace_id()
        logger.configure_logger(trace_id)

        # This is the authentication process for the lambda itself
        # Note: environment variable BIOT_SHOULD_VALIDATE_JWT should be false if the lambda does not receive a token, otherwise authentication will fail the lambda
        if BIOT_SHOULD_VALIDATE_JWT == True:
            authenticate(event_token, trace_id)

        # Here we are requesting a token for the lambda
        # It is done using a service users BIOT_SERVICE_USER_ID and BIOT_SERVICE_USER_SECRET_KEY that should be set to an environment variable
        token = login(trace_id)

        # Some of the properties sent to perform might not be relevant, depending on the type of lambda or lambda hook used to invoke it
        response = perform(
            data,
            token,
            trace_id,
            metadata
        )

        return response
    except Exception as error:
        # This should return the proper error responses by the type of error that occurred
        # See the createErrorResponse function for your specific lambda usage
        return create_error_response(error, trace_id)

