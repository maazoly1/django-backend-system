.PHONY: run dev
run dev:
	poetry run python -m app.manage runserver

.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m app.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m app.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m app.manage createsuperuser

# Shorter commands for pre commit command
.PHONY: lint
lint:
	poetry run pre-commit --all-files

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall;
	poetry run pre-commit install;

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no 

.PHONY: docker-db
docker-db:
	test -f .env || touch .env;
	docker-compose -f docker-compose.dev.yml up --force-recreate db;

.PHONY: update
update: install migrate install-pre-commit ;



