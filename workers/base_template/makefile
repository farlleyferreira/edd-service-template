
setup-lib:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	python -m black .

run:
	python ./source/main.py

run-tests:
	python -m pytest

run-coverage:
	python  -m pytest -v --cov-report term-missing --cov=./source/ --cov-report=xml 