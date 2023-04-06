# Integrating With SpiffArena

## Prerequisites

1. You've gone through the [Getting Started Guide](https://www.spiffworkflow.org/posts/articles/get_started/) or have otherwise set up an installation of SpiffArena.
2. You have access to login to the AWS Console and can create Lambda functions.
3. You want to see how cool it is to communicate with external systems from SpiffArena.

## Service Tasks and Connector Proxies

When authoring a BPMN diagram, `Service Tasks` are used to communicate with external systems. By leveraging Service Tasks workflows can make http based api calls, write files to S3, find an employee's manager via the HR system or send a fax. The response from the external system is available to your workflow for future handling.

While a Service Task provides the BPMN diagram author with the means of configuring how and when SpiffArena should communicate with an external system, a `Connector Proxy` is required to perform the actual communication. The reasons for this are:

1. Decouple dependencies required to talk to any system from those required to execute workflows.
2. Allow for communication with pre-existing sdks that may not be written in Python.
3. Provide a uniform way for BPMN diagram authors to configure communication to external systems


