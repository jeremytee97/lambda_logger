# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['before_send', 'capture_error', 'logger']

# Cell
from sentry_sdk import configure_scope, capture_event, capture_exception, set_tag
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from aws_lambda_powertools import Logger

import sentry_sdk
import sys
import os

def before_send(event, hint):
    if 'exc_info' not in hint:
        return event

    exception = hint['exc_info'][1]
    if isinstance(exception, str):
        event['fingerprint'] = ['str-error-messages']
    elif isinstance(exception, dict):
        event['fingerprint'] = ['dict-error-messages']
    elif isinstance(exception, list):
        event['fingerprint'] = ['list-error-messages']
    return event


sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        environment=os.environ["SERVERLESS_STAGE"],
        integrations=[AwsLambdaIntegration()],
        before_send=before_send)

set_tag("project", os.environ["PROJECT_NAME"])
set_tag("fn_name", os.environ["FN_NAME"])

logger = Logger(service=os.environ["FN_NAME"], level="INFO")

# Logging an exception
def capture_error(error, method, context=None):
    logger.error(error, {"method":method, "context": context})
    if (os.environ["SERVERLESS_STAGE"] == "sandbox" or os.environ["SERVERLESS_STAGE"] == "production"):
        with configure_scope() as scope:
            scope.set_tag("method", method)
            if (context is not None):
                scope.set_extra("context", context)
        capture_exception(error)