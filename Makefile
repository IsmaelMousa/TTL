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
	@echo "http://localhost:8000/ttl/index.html"
	@python3 main.py