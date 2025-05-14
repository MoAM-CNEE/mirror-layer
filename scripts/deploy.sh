#!/bin/bash

AWAIT_INSTALL_COMPLETION_S=120
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
MANIFESTS_DIR="$SCRIPT_DIR/../manifests"

cd "$MANIFESTS_DIR"

kubectl apply -f 00-ns.yaml

helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
helm upgrade --install crossplane \
--namespace mirror-layer \
--create-namespace crossplane-stable/crossplane

OPENSTACK_CONFIG_PATH=openstack-auth-config.json && \
kubectl --namespace mirror-layer create secret generic openstack-auth-config --from-file=config=$OPENSTACK_CONFIG_PATH

KUBE_CONFIG_PATH=kubeconfig && \
kubectl --namespace mirror-layer create secret generic kubeconfig --from-file=kubeconfig=$KUBE_CONFIG_PATH

echo "> Await install completion for $AWAIT_INSTALL_COMPLETION_S s"
sleep $AWAIT_INSTALL_COMPLETION_S

kubectl apply -f 01-control-plane-providers.yaml

echo "> Await install completion for $AWAIT_INSTALL_COMPLETION_S s"
sleep $AWAIT_INSTALL_COMPLETION_S

kubectl apply -f 02-control-plane-provider-configs.yaml
kubectl apply -f 03-mirror-manager.yaml
