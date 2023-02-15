import json

from spiffworkflow_proxy.plugin_service import PluginService

def lambda_handler(event, context):
    raw_path = event.get("rawPath", "")
    result = {
        "statusCode": 404,
        "body": "Not found."
    }
    if raw_path == "/":
        result = route_index(event, context)
    elif raw_path == "/v1/commands":
        result = route_v1_commands(event, context)

    result["body"] = json.dumps(result["body"])

    return result

def route_index(event, context):
    return {
        "statusCode": 200,
        "body": "This is the SpiffWorkflow Connector.   Point SpiffWorkfow-backend configuration to this url." \
           " Please see /v1/commands for a list of commands this connector proxy will allow.",
    }

def route_v1_commands(event, context):
    commands = _list_targets(PluginService.available_commands_by_plugin())
    return {
        "statusCode": 200,
        "body": commands,
    }


def _list_targets(targets):
    descriptions = []

    for plugin_name, plugin_targets in targets.items():
        for target_name, target in plugin_targets.items():
            description = PluginService.describe_target(
                plugin_name, target_name, target
            )
            descriptions.append(description)

    return descriptions
