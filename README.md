# connector-proxy-lambda-demo

Demo showing how a serverless connector proxy could be deployed as an AWS Lambda Function for use by Spiff Arena.

## Without Docker

Install dependencies:

```
poetry install
```

Build the artifact to upload:

```
./make_zip.sh
```

To deploy from the AWS Lambda Console:

Create a new lambda function with a publicly available function url. Choose upload from zip and select `artifact.zip` from the root directory of this demo. Click on the function url link above the code editor and your connector proxy is live.

## With Docker

```
docker build -t lambda_demo .
```

To test:

```
docker run -p 9000:8080 lambda_demo
```

In another terminal:

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"rawPath": "/"}'
```

I have not gone through the motions yet of uploading to ECR/configuring a lamba with the container image.

### Some notes

This is a demo and only has an http get and post connector currently. If this were used outside of a demo it would be nice to be able to opt out of the flask portions of `spiffworkflow-proxy` or extract the `PluginService` to reduce the deployment size.
