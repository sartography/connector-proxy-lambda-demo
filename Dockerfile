FROM public.ecr.aws/lambda/python:3.9

WORKDIR ${LAMBDA_TASK_ROOT}

RUN yum -y update && \
    yum -y install \
        git

COPY pyproject.toml poetry.lock README.md ./
COPY connector_proxy_lambda_demo/*.py ./connector_proxy_lambda_demo/

RUN pip3 install poetry
RUN poetry install
RUN poetry build
RUN poetry run pip3 install -t . dist/*.whl

# Copy function code
COPY connector_proxy_lambda_demo/lambda_function.py .

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ]
