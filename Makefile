setup-local-python: clean-venv
	pip3 install virtualenv; \
	virtualenv venv --python=python3.8; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \
	pip3 install -r requirements-dev.txt;

clean-venv:
	rm -rf venv

lint:
	. ./venv/bin/activate; \
	python3 -m flake8 .

check-imports:
	. ./venv/bin/activate; \
	python -m isort . --skip venv --skip logs --check-only

fix-imports:
	. ./venv/bin/activate; \
	python -m isort . --skip venv --skip logs


events-pipeline-down:
	docker-compose down

events-pipeline-up: events-pipeline-down
	docker-compose up --build

clean-metadata-db:
	rm -rf postgres_data

clear-local:
	rm -rf logs
	rm -f airflow.cfg
	rm -f airflow.db
	rm -f unittests.cfg

init-local:
	./local/init