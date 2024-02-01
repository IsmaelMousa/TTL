help h:
	@echo "Available Commands:"
	@sed -n "/^[a-zA-Z0-9_.]*:/s/:.*//p" < Makefile | GREP_COLOR="01;34" grep --color=always -E "^[a-zA-Z0-9_.]*"

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

# Just For GitHub!
ci_test:
	@pytest --cache-clear --ignore tests/routers_task.py

ci_coverage:
	@pytest --cache-clear --cov --cov-report=term-missing --ignore tests/routers_task.py

