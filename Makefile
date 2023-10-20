install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=search_engine --cov-report xml

lint:
	poetry run flake8

check: test lint

.PHONY: install test lint check