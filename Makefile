install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	poetry run flake8

check: test lint

.PHONY: install test lint check