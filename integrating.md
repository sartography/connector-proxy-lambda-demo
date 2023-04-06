# Deploying and Integrating With SpiffArena

This guide shows you how to deploy the demo `Connector Proxy` as an `AWS Lambda Function` as well as how to integrate it with [SpiffArena](https://www.spiffworkflow.org/pages/spiffarena/). The [Getting Started Guide](https://www.spiffworkflow.org/posts/articles/get_started/) will be used as the basis for integration but the steps should easily map to any custom installation.

There is an assumption that you have access to login to the AWS Console and can create/deploy Lambda functions.

## Building the zip

One option when deploying a Lambda function is to upload a zip file containing the source code or executable. Since that is pretty straightforward we will be using that option for this demo. In the root of this repository run:

```
make zip
```

This will create a zip file containing the lambda entry point function as well as all the dependencies needed to execute the connectors. For this example the libraries [spiffworkflow-proxy](https://github.com/sartography/spiffworkflow-proxy) is used for discovering connectors and [connector-http](https://github.com/sartography/connector-http) is an example connector that provides http get and post requests.


### Old stuff below

3. You want to see how cool it is to add integrations with external systems from SpiffArena.

## Service Tasks and Connector Proxies Recap

When authoring a BPMN diagram, `Service Tasks` are used to communicate with external systems. By leveraging Service Tasks workflows can make http based api calls, write files to S3, find an employee's manager via the HR system or send a fax. The response from the external system is available to your workflow for future handling.

While a Service Task provides the BPMN diagram author with the means of configuring how and when SpiffArena should communicate with an external system, a `Connector Proxy` is required to perform the actual communication. The reasons for this are:

1. Decouple dependencies required to talk to any system from those required to execute workflows.
2. Allow for communication with pre-existing sdks that may not be written in Python.
3. Provide a uniform way for BPMN diagram authors to configure communication to external systems

## 
