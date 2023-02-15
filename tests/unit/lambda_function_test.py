import json

from connector_proxy_lambda_demo.lambda_function import lambda_handler

def test_index():
    event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/', 'rawQueryString': ''}
    context = {}
    result = lambda_handler(event, context)
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body.startswith("This is the SpiffWorkflow Connector.")

def test_404():
    event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/bob', 'rawQueryString': ''}
    context = {}
    result = lambda_handler(event, context)
    assert result["statusCode"] == 404
    body = json.loads(result["body"])
    assert body == "Not found."

def test_v1_commands():
    event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/v1/commands', 'rawQueryString': ''}
    context = {}
    result = lambda_handler(event, context)
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert len(body) == 2
