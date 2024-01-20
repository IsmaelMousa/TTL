help h:
	@echo "Available Commands:"
	@sed -n '/^[a-zA-Z0-9_.]*:/s/:.*//p' < Makefile

install:
	@echo "Installing Dependencies..."
	@pip install poetry
	@poetry config virtualenvs.in-project true
	@poetry install --no-root

lint:
	@echo "Check Linting..."
	@pylint "**/*.py"
test:
	@pytest --cache-clear

coverage:
	@pytest --cache-clear --cov --cov-report=term-missing

run:
	@uvicorn main:app --reload