LAMBDA_CONTAINER := connector-proxy-lambda-demo
LAMBDA_SERVICE := lambda

.PHONY: all
all: start

.PHONY: build
build:
	docker compose build

.PHONY: start
start: stop build
	docker compose up -d

.PHONY: stop
stop:
	docker compose down

.PHONY: shell
shell:
	docker exec -it $(LAMBDA_CONTAINER) /bin/bash

.PHONY: request-index
request-index:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"rawPath": "/"}'
