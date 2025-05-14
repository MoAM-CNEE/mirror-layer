.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

deploy: ## deploy to the Kubernetes cluster
	./scripts/deploy.sh

get-minikube-secrets: ## print Minikube secrets to be substituted in kubeconfig
	./scripts/get_minikube_secrets.sh
