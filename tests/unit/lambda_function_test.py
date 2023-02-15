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

# TODO: move to integration test
def test_do_command():
    event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/v1/do/http/GetRequest', 'rawQueryString': '', 'requestContext': {'http': {'method': 'POST', 'path': '/v1/do/http/GetRequest', 'protocol': 'HTTP/1.1'}, 'routeKey': '$default', 'stage': '$default'}, 'body': '{"url": "http://www.google.com", "headers": [], "params": null, "basic_auth_username": null, "basic_auth_password": null}', 'isBase64Encoded': False}
    context = {}
    result = lambda_handler(event, context)
    assert result["statusCode"] == 200
