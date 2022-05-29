SHELL:=/bin/bash

VERSION=`cat VERSION`

.PHONY: docker-image
build-img:
	docker build -f Dockerfile -t video-content-miner: .
	
rm-img:
	docker rmi video-content-miner:$(VERSION)

.PHONY: server
up:
	export VERSION=$(VERSION) \
	&& docker-compose -f docker-compose.yml up -d --remove-orphans
up-build:
	export VERSION=$(VERSION) \
	&& docker-compose -f docker-compose.yml up --build -d --remove-orphans
down:
	export VERSION=$(VERSION) \
	&& docker-compose -f docker-compose.yml down --remove-orphans
pkg-version:
	echo "$(VERSION)"
