DOCKERHUB_USERNAME=proman3419
IMAGE_NAME=mirror-manager
VER=0.0.0.1

build:
	docker build -t $(DOCKERHUB_USERNAME)/$(IMAGE_NAME):$(VER) .

push:
	docker login
	docker push $(DOCKERHUB_USERNAME)/$(IMAGE_NAME):$(VER)
