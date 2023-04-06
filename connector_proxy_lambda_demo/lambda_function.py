import json

from spiffworkflow_proxy.plugin_service import PluginService

def lambda_handler(event, context):
    raw_path = event.get("rawPath", "")
    result = None
    if raw_path == "/":
        result = route_index(event, context)
    elif raw_path == "/v1/commands":
        result = route_v1_commands(event, context)
    elif raw_path.startswith("/v1/do/"):
        result = route_do_command(event, context)

    if result is None:
        result = {
            "statusCode": 404,
            "body": json.dumps("Not found.")
        }

    return result

def route_index(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("This is the SpiffWorkflow Connector, lambda demo version. " \
                           " Point SpiffWorkfow-backend configuration to this url." \
                           " Please see /v1/commands for a list of commands this connector proxy will allow."),
    }

def route_v1_commands(event, context):
    commands = _list_targets(PluginService.available_commands_by_plugin())
    return {
        "statusCode": 200,
        "body": json.dumps(commands),
    }

def route_do_command(event, context):
    parts = event["rawPath"].split("/")
    if len(parts) != 5:
        return None

    request_context = event["requestContext"]
    method = request_context["http"]["method"]

    if method != "POST":
        return

    plugin_display_name = parts[3]
    command_name = parts[4]
    command = PluginService.command_named(plugin_display_name, command_name)
    if command is None:
        return None

    params = json.loads(event.get("body", "{}"))
    task_data = params.pop('spiff__task_data', '{}')
    result = command(**params).execute({}, task_data)

    return {
        "statusCode": result["status"],
        "body": result["response"],
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
