install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov-report term-missing --cov=gendiff

setup: install build package-install