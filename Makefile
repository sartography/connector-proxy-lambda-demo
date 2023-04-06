
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

.PHONY: request-index
request-index:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"rawPath": "/"}'

.PHONY: request-commands
request-commands:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"rawPath": "/v1/commands"}'

.PHONY: zip
zip: build
	set -e ;\
	TMP_ID=$$(docker create connector-proxy-lambda-demo-lambda) ;\
	docker cp $$TMP_ID:/zip/connector_proxy_lambda_demo.zip . ;\
	docker rm -v $$TMP_ID ;\
