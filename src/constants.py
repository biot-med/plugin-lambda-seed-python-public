import os


API_CALL_ERROR = "CALL_TO_API_FAILED"
JWT_ERROR = "JWT_ERROR"
NO_EVENT_ERROR = "NO_EVENT"
NO_METADATA_ERROR = "NO_METADATA"
NO_DATA_ERROR = "NO_DATA"

def resolve_should_validate(env_var):
    if env_var is not None:
        if env_var == "False" or env_var == "false":
            return False
        else:
            return True
    else:
        return True


cloud_constants = {
    "BIOT_PUBLIC_KEY": os.getenv("BIOT_PUBLIC_KEY"),
    "BIOT_JWT_PERMISSION": os.getenv("BIOT_JWT_PERMISSION_NOTIFICATION") if os.getenv("BIOT_JWT_PERMISSION_NOTIFICATION") is not None else os.getenv("BIOT_JWT_PERMISSION_INTERCEPTION"),
    "BIOT_APP_NAME": os.getenv("BIOT_APP_NAME"),
    "BIOT_BASE_URL": os.getenv("BIOT_BASE_URL"),
    "BIOT_SERVICE_USER_ID": os.getenv("BIOT_SERVICE_USER_ID"),
    "BIOT_SERVICE_USER_SECRET_KEY": os.getenv("BIOT_SERVICE_USER_SECRET_KEY"),
    "AWS_EXECUTION_ENV": os.getenv("AWS_EXECUTION_ENV"),
    "BIOT_SHOULD_VALIDATE_JWT": resolve_should_validate(os.getenv("BIOT_SHOULD_VALIDATE_JWT")),
    "BIOT_SERVICE_ENVIRONMENT": os.getenv("BIOT_SERVICE_ENVIRONMENT")
}

local_dev_constants = {
    "BIOT_PUBLIC_KEY": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu8kO8u5hNmkvZnGWaTjWvHGvHDnz+5WkfBImOB3aQCDcGZ/schJNVF0ANRrA8lXwWXOdYC0cVkElVEaAy1wHcqhCKhp6qCTWo19eMIAAnILSwcDWtaLPyDIMDOQJqts24c76ODJV8qJ2zC/zKSrBMt9lSuwP2ms8ZzgQ0UQzpWd950xf5f/pxsRhaxboQtBWhUmzEstHB1bHiaElFgM3ct0shDZ8I9QplxtAQQrzZ8gFaaVZcT0oi1h8BMU9wdPS4+KDisQ4ai2Bka7bxGNuhC9U8/gyidNZbDrO7emlOWKxLB8CCeYRb+bl+x1nm+jfNRzXZdOk/nXyRtAZfCRbGQIDAQAB",
    "BIOT_JWT_PERMISSION": None,
    "BIOT_APP_NAME": "BioT Lambda seed",
    "BIOT_BASE_URL": None,
    "BIOT_SERVICE_USER_ID": None,
    "BIOT_SERVICE_USER_SECRET_KEY": None,
    "AWS_EXECUTION_ENV": "DEV",
    "BIOT_SHOULD_VALIDATE_JWT": None,
    "BIOT_SERVICE_ENVIRONMENT": "gen2int",
}

environment_constants = cloud_constants if os.getenv("AWS_EXECUTION_ENV") is not None else local_dev_constants

# This prepares the BIOT_PUBLIC_KEY to be used with jsonwebtoken's parse (in authenticate function)
BIOT_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + environment_constants["BIOT_PUBLIC_KEY"] + "\n-----END PUBLIC KEY-----"

BIOT_JWT_PERMISSION = environment_constants["BIOT_JWT_PERMISSION"]
BIOT_APP_NAME = environment_constants["BIOT_APP_NAME"]
BIOT_BASE_URL = environment_constants["BIOT_BASE_URL"]
BIOT_SERVICE_USER_ID = environment_constants["BIOT_SERVICE_USER_ID"]
BIOT_SERVICE_USER_SECRET_KEY = environment_constants["BIOT_SERVICE_USER_SECRET_KEY"]
AWS_EXECUTION_ENV = environment_constants["AWS_EXECUTION_ENV"]
BIOT_SHOULD_VALIDATE_JWT = environment_constants["BIOT_SHOULD_VALIDATE_JWT"]
BIOT_SERVICE_ENVIRONMENT = environment_constants["BIOT_SERVICE_ENVIRONMENT"]
