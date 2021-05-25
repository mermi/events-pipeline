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
