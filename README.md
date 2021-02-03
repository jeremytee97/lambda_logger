# Lambda_logger
> to log the process of the lambda to AWS cloudwatch, and log error to Sentry


## Install

`pip install lambda-logger`

## How to use

Add the following Environment Variable to your serverless.yml

- SENTRY_DSN
- SERVERLESS_STAGE (production/sandbox)
- PROJECT_NAME
- FN_NAME

```python
from lambda_logger.core import capture_exception

capture_exception(Error, method, context)
```
![alt text](https://github.com/jeremytee97/lambda_logger/blob/master/docs/sentry_image.PNG?raw=true)
---- 

For logging info level

Refer to https://github.com/awslabs/aws-lambda-powertools-python for more examples
```python
from lambda_logger.core import logger
logger.info("message", {"key": "value"})
```

```
{
    "level": "INFO",
    "location": "invoke_ld:51",
    "message": "invoke_lambda",
    "timestamp": "2021-02-03 07:11:05,304",
    "service": "des-prediction-nominator",
    "sampling_rate": 0,
    "xray_trace_id": "1-601a4c86-67543c3e450432f739ab28f0"
}
```
