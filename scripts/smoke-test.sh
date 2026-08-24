#!/usr/bin/env bash

set -euo pipefail

NAMESPACE="${NAMESPACE:-canary-demo}"
SERVICE="${SERVICE:-product-stable}"

echo "Running smoke test"
echo "Namespace : ${NAMESPACE}"
echo "Service   : ${SERVICE}"

kubectl run smoke-test \
  -n "${NAMESPACE}" \
  --rm \
  -i \
  --restart=Never \
  --image=curlimages/curl:8.10.1 \
  -- \
  curl -fsS "http://${SERVICE}/"
