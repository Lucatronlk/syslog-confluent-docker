#!/bin/bash

connector_name=$1
start_time=$(date +%s)
end_time=$((start_time + 600))

while [[ $(date +%s) -lt $end_time ]]; do
    echo "$(date +'%Y-%m-%dT%H:%M:%S') Sample $connector_name message" >> /dev/udp/localhost/514
    sleep 5
done
