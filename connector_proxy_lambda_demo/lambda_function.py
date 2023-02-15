import json

def lambda_handler(event, context):
    raw_path = event.get("rawPath", "")
    result = {
        "statusCode": 404,
        "body": "Not found."
    }
    if raw_path == "/":
        result = _index(event, context)
    elif raw_path == "/v1/commands":
        result = _commands(event, context)

    result["body"] = json.dumps(result["body"])

    return result

def _index(event, context):
    return {
        "statusCode": 200,
        "body": "This is the SpiffWorkflow Connector.   Point SpiffWorkfow-backend configuration to this url." \
           " Please see /v1/commands for a list of commands this connector proxy will allow."
    }

def _commands(event, context):
    return {
        "statusCode": 200,
        "body": []
    }

