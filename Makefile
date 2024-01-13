install:
	@echo "========================== Install Dependencies ===========================\n"
	@pip install poetry
	@poetry config virtualenvs.in-project true
	@poetry install --no-root
	@echo "================================== Done ==================================="

lint:
	@echo "========================== Check linting ===========================\n"
	@(pylint '**/*.py' && echo "=============================== Pass ===============================") || echo "=============================== Fail ==============================="

test:
	@pytest

coverage:
	@pytest --cov --cov-report=term-missing

run:
	@echo "============================= Uvicorn Running ============================="
	@uvicorn main:app --reload