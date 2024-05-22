from src.utils.call_to_api_example import call_api_example
from src.utils.configure_logger import logger


def perform(data, token, traceparent, metadata):
    # -----------------------------------------------------------------------------------------

    # TODO: ADD YOUR CODE HERE !
    # Remove this example call and add your code instead

    # This is an example of changing on of the entities in the response
    # You can change any response value you want

    changed_data = data 

    if "firstName" in changed_data["body"]["response"]["entities"][0]["_name"]:
        changed_data["body"]["response"]["entities"][0]["_name"]["firstName"] = changed_data["body"]["response"]["entities"][0]["_name"]["firstName"] + " LAMBDA" 

    # This is an example of calling a BioT API (using the token from the service users token)
    # In this case we are making a get patients request to organization API

    call_example_response = call_api_example(token, traceparent)

    # In this example you perform your logic with the response Here

    logger.info("In post entity lambda, got callExampleResponse ", call_example_response)

    # -----------------------------------------------------------------------------------------

    return {"response": changed_data["body"]["response"]}
