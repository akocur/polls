MANAGE := poetry run python manage.py

install:
	poetry install
test-django:
	@$(MANAGE) test
lint:
	poetry run flake8
selfcheck:
	poetry check
check: selfcheck test lint
build: check
	poetry build
install-package: build
	python3 -m pip install --user .
makemigrations:
	@$(MANAGE) makemigrations
migrate: makemigrations
	@$(MANAGE) migrate
shell:
	@$(MANAGE) shell_plus --ipython
run:
	@$(MANAGE) runserver

.PHONY: install test lint selfcheck check build makemigrations migrate shell
