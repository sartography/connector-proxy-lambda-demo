FROM public.ecr.aws/lambda/python:3.9 AS build

# install git so poetry/pip can install spiffworkflow-proxy and connector-http
RUN yum -y update && \
    yum -y install \
        git

WORKDIR ${LAMBDA_TASK_ROOT}

COPY pyproject.toml poetry.lock README.md ./
COPY connector_proxy_lambda_demo/*.py ./connector_proxy_lambda_demo/

RUN pip3 install poetry
RUN poetry install
RUN poetry build
RUN poetry run pip3 install -t ./package dist/*.whl

FROM public.ecr.aws/lambda/python:3.9 AS final

WORKDIR ${LAMBDA_TASK_ROOT}

# copy all dependencies installed during the build into the task root
COPY --from=build /${LAMBDA_TASK_ROOT}/package ./

# copy the lambda function into the task root
COPY connector_proxy_lambda_demo/lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]
