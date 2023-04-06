# Integrating With SpiffArena

## Prerequisites

1. You've gone through the [Getting Started Guide](https://www.spiffworkflow.org/posts/articles/get_started/) or have otherwise set up an installation of SpiffArena.
2. You have access to login to the AWS Console and can create Lambda functions.
3. You want to see how cool it is to communicate with external systems from SpiffArena.

## Service Tasks and Connector Proxies

When authoring a BPMN diagram, Service Tasks are used to communicate with external systems. An example of this would be making an http get request to find the current weather for a given zipcode or performing an http post to submit results of a running process to another system. 
