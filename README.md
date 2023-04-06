# connector-proxy-lambda-demo

Demo showing how a serverless connector proxy could be deployed as an AWS Lambda Function for use by Spiff Arena.

Requires docker and docker compose.

## To deploy from the AWS Lambda Console:

In the root of this project run:

```
make zip
```

Create a new lambda function with a publicly available function url. Choose upload from zip and select `connector_proxy_lambda_demo.zip` from the root directory of this demo. Click on the function url link above the code editor and your connector proxy is live.

## Local Testing

```
make start
```

Will start the lambda development server locally on port 9000. Two example requests are baked in to the `Makefile`.

```
make request-index
```

```
make request-commands
```

These will confirm the lambda function is responding correctly locally. When done:

```
make stop
```

If you just want to build the docker image:

```
make build
```

I have not gone through the motions yet of uploading to ECR/configuring a lamba with the container image.

### Some notes

This is a demo and only has an http get and post connector currently. If this were used outside of a demo it would be nice to be able to opt out of the flask portions of `spiffworkflow-proxy` or extract the `PluginService` to reduce the deployment size. It would also be beneficial to extract the lambda routing logic into its own package.
