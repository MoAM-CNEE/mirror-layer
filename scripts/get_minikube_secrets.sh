#!/bin/bash

read -r -d '' INPUT << EOM
certificate-authority: /home/przemek/.minikube/ca.crt
client-certificate: /home/przemek/.minikube/profiles/minikube/client.crt
client-key: /home/przemek/.minikube/profiles/minikube/client.key
EOM

while IFS=':' read -r key path; do
    key=$(echo "$key" | xargs)
    path=$(echo "$path" | xargs)

    if [[ -f "$path" ]]; then
        encoded=$(base64 -w 0 "$path")
        echo "$key-data: $encoded"
        echo ""
    else
        echo "FILE NOT FOUND ($path)" >&2
        echo ""
    fi
done <<< "$INPUT"
