.PHONY: help

DOCKERHUB_USERNAME=proman3419
IMAGE_NAME=mirror-manager
VER=0.0.0.1

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## build - result accessible through local repository
	docker build -t $(DOCKERHUB_USERNAME)/$(IMAGE_NAME):$(VER) .

build-and-push-final: ## !RUN ONLY ON MASTER! build-and-push-non-final + tag the commit with VER
	make build-and-push-non-final
	git tag v$(VER)
	git push origin --tags

build-and-push-non-final: ## build and push to DockerHub
	docker build -t $(DOCKERHUB_USERNAME)/$(IMAGE_NAME):$(VER) .
	docker login
	docker push $(DOCKERHUB_USERNAME)/$(IMAGE_NAME):$(VER)

.DEFAULT_GOAL := help
