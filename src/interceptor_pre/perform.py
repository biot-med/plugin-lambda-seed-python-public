from src.utils.configure_logger import logger
from src.utils.call_to_api_example import call_api_example


def perform(data, token, trace_id):
    # -----------------------------------------------------------------------------------------

    # TODO: ADD YOUR CODE HERE !
    # Remove this example call and add your code instead

    # This is an example of changing the request
    # You can change any request value you want

    changed_data = data

    if "firstName" in changed_data["body"]["request"]["body"]["_name"]:
        changed_data["body"]["request"]["body"]["_name"]["firstName"] = changed_data["body"]["request"]["body"]["_name"]["firstName"] + " LAMBDA MODIFIED"
   

    # This is an example of calling a BioT API (using the token from the service users token)
    # In this case we are making a get patients request to organization API

    call_example_response = call_api_example(token, trace_id)

    # In this example you perform your logic with the response Here

    logger.info("In pre interceptor lambda, got callExampleResponse ", call_example_response)

    # -----------------------------------------------------------------------------------------

    return changed_data["body"]
