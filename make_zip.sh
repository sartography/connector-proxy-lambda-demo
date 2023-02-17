#!/bin/sh

rm -f archive.zip

# https://chariotsolutions.com/blog/post/building-lambdas-with-poetry/
poetry run pip install --upgrade -t package dist/*.whl
cd package
cp ../connector_proxy_lambda_demo/lambda_function.py .
zip -r ../artifact.zip . -x '*.pyc'
