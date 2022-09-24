#!/bin/bash
OPENAPI_PATH="openapi.json"
OUT_PATH="tmp"
PACKAGE_NAME="sitreps_python_api"
podman run --rm -v $PWD:/local:Z openapitools/openapi-generator-cli generate -i /local/$OPENAPI_PATH -g python -o /local/$OUT_PATH --package-name $PACKAGE_NAME
rm -r $PACKAGE_NAME
mv $OUT_PATH/$PACKAGE_NAME .
rm -r docs
mv $OUT_PATH/docs .
rm -r test
mv $OUT_PATH/test .

