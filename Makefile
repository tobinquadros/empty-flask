include .env
IMAGE_NAME=$(ORGANIZATION)/$(APP_NAME)

.PHONY: app test build check dashboards clean rm-containers rm-images

app:
	docker-compose up app

test:
	docker-compose run app /code/bin/run_tests

build:
	docker image build -t $(IMAGE_NAME) .

check:
	@ bin/check $(HOST_PORT)

dashboards:
	@ docker-compose up

rm-containers:
	-@ docker-compose down --remove-orphans

rm-images:
	-@ docker image ls -aq -f "dangling=true" -f "reference=$(IMAGE_NAME)*" | xargs -I {} docker image rm -f {}
	-@ docker-compose down --rmi local -v

clean: rm-containers rm-images
