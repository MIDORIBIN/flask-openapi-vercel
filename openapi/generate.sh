#!/bin/bash

cd "$(dirname "$0")"

/usr/local/bin/docker-entrypoint.sh generate -i /openapi_server/openapi/openapi.yaml -g python-flask -o /tmp/out
rm -r /openapi_server/*
cp -r /tmp/out/openapi_server/* /openapi_server
