CONTAINER_NAME = app
RUN_APP = docker-compose exec $(CONTAINER_NAME)
RUN_POETRY =  $(RUN_APP) poetry run

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

clean:
	docker-compose down --rmi all --volumes --remove-orphans

show_report:
	open $(REPORT_URL)

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .

update:
	$(RUN_APP) poetry update

app:
	docker exec -it ${CONTAINER_NAME} bash
