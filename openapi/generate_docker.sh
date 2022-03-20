#!/bin/bash

cd "$(dirname "$0")"

docker run --rm \
  -v ${PWD}/../openapi_server:/openapi_server \
  -v ${PWD}/generate.sh:/generate.sh:ro \
  openapitools/openapi-generator-cli:v5.4.0 \
  /generate.sh
