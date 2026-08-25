#!/bin/bash

set -e

echo "Checking product service..."

for i in $(seq 1 10); do

    response=$(curl -s http://product)

    echo "Request $i: $response"

    if [ -z "$response" ]; then
        echo "ERROR: Empty response"
        exit 1
    fi

done

echo "Smoke test passed"
