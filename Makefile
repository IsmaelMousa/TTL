install:
	@echo "========================== Install Dependencies ===========================\n"
	@poetry install --only main
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