update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements-dev.txt

pre-commit-install:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

commitizen-init:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog
