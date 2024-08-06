from src.utils.call_to_api_example import call_api_example
from src.utils.configure_logger import logger
from src.utils.generic_success_response import generic_success_response


def perform(data, token, traceparent, metadata):
    # -----------------------------------------------------------------------------------------

    # TODO: ADD YOUR CODE HERE !

    # This is an example of calling a BioT API (using the token from the service users token)
    # In this case we are making a get patients request to organization API
    # Remove this example call and add your code instead

    call_example_response = call_api_example(token, traceparent)

    # In this example you perform your logic with the response Here

    logger.info("In post interceptor lambda, got callExampleResponse ", call_example_response)

    changed_data = data  # change the data according to your logic

    # -----------------------------------------------------------------------------------------
    return {"response": changed_data["body"]["response"]}
