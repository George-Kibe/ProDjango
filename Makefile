# target: prereqs
# 	recipe
# .PHONY means the command doesnt have to check if there is a file or prevent file conflicts
# .PHONY helps improve on performance

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python3 -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python3 -m core.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python3 -m core.manage runserver

.PHONY: shell
shell:
	poetry run python3 -m core.manage shell

.PHONY: superuser
superuser:
	poetry run python3 -m core.manage createsuperuser

# -v for verbose -rs report s-skipped -n for as many cores as possible --show-capture=no not to show outputs
.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrations migrate install-pre-commit ;
