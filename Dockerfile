FROM public.ecr.aws/lambda/python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.

#COPY requirements.txt  .
#RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

WORKDIR ${LAMBDA_TASK_ROOT}

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
