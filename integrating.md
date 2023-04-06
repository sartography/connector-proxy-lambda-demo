# Deploying and Integrating With SpiffArena

This guide shows you how to deploy the demo `Connector Proxy` as an `AWS Lambda Function` as well as how to integrate it with [SpiffArena](https://www.spiffworkflow.org/pages/spiffarena/). The [Getting Started Guide](https://www.spiffworkflow.org/posts/articles/get_started/) will be used as the basis for integration but the steps should easily map to any custom installation.

There is an assumption that you have access to login to the AWS Console and can create/deploy Lambda functions.

## Building the zip

One option when deploying a Lambda function is to upload a zip file containing the source code or executable. In the root of this repository run:

```
make zip
```

This will create a zip file containing the [lambda entry point function](https://github.com/jbirddog/connector-proxy-lambda-demo/blob/main/connector_proxy_lambda_demo/lambda_function.py#L5) as well as all the dependencies needed to execute the connectors. For this example the libraries [spiffworkflow-proxy](https://github.com/sartography/spiffworkflow-proxy) is used for discovering connectors and [connector-http](https://github.com/sartography/connector-http) is an example connector that provides http get and post requests.

Once `make zip` completes `connector_proxy_lambda_demo.zip` will be available in the repository root.

## Deploying the Lambda Function

Log in to the AWS Console and navigate to the Lambda section. 

![Screenshot from 2023-04-06 15-19-35](https://user-images.githubusercontent.com/100367399/230482600-bf5f72b4-f499-4d44-8f6b-814d8e4c67d2.png)

From there choose `Create function`.

![Screenshot from 2023-04-06 15-22-39](https://user-images.githubusercontent.com/100367399/230482607-ad561180-9a4d-4ad1-8e4c-c97903f99100.png)

Choose to `Author from scratch` and select the most recent Python runtime.

![Screenshot from 2023-04-06 15-23-19](https://user-images.githubusercontent.com/100367399/230482609-8bece818-a41f-4f37-99c4-d9d10bef4d54.png)

Under `Advanced Settings` check `Enable function URL`. For this demo we will use the `NONE` auth type to keep things simple.

![Screenshot from 2023-04-06 15-24-12](https://user-images.githubusercontent.com/100367399/230482613-8fa6c8ef-5035-4a77-9670-f7211bf92cc0.png)

After hitting the `Create function` button you will be taken to your new Lambda function:

![Screenshot from 2023-04-06 16-02-11](https://user-images.githubusercontent.com/100367399/230482618-cf4cf088-3629-4832-9a3d-d81f29842aff.png)

