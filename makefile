IMG=f4prime/pvinit:v0.0.1
all: docker-build docker-push
	echo done

docker-build:
	docker build . -t $(IMG)

docker-push:
	docker push $(IMG)

