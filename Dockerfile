FROM public.ecr.aws/lambda/python:3.10 AS build

# install git so poetry/pip can install spiffworkflow-proxy and connector-http
RUN yum -y update && \
    yum -y install \
        git \
	zip

WORKDIR /build

COPY pyproject.toml poetry.lock README.md ./
COPY connector_proxy_lambda_demo/*.py ./connector_proxy_lambda_demo/

RUN pip3 install poetry
RUN poetry install

RUN poetry build
RUN poetry run pip3 install -t ./package dist/*.whl

# build the zip that will be uploaded to aws
RUN cd package && \
    cp ../connector_proxy_lambda_demo/lambda_function.py . && \
    zip -r ../connector_proxy_lambda_demo.zip . -x '*.pyc'

# TODO: run tests

FROM public.ecr.aws/lambda/python:3.10 AS final

WORKDIR /zip

COPY --from=build /build/connector_proxy_lambda_demo.zip .

WORKDIR ${LAMBDA_TASK_ROOT}

# copy all dependencies installed during the build into the task root
COPY --from=build /build/package ./

# copy the lambda function into the task root
COPY connector_proxy_lambda_demo/lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]
