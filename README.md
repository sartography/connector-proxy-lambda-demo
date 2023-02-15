# connector-proxy-lambda-demo

Demo showing how a serverless connector proxy could be deployed as an AWS Lambda Function for use by Spiff Arena.

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

### Some notes

This is a demo and only has an http get and post connector currently. It also requires minor changes to be merged upstream to the `spiffworflow-proxy` and `connector-http` packages since Lambda functions require Python 3.9. If this were used outside of a demo it would be nice to be able to opt out of the flask portions of `spiffworkflow-proxy` or extract the `PluginService` to reduce the deployment size.
