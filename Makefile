# Windows 上没有 make 时用 scripts/dev.ps1，见 README。
PY_BACKEND := backend/.venv/Scripts/python.exe

.PHONY: setup run test lint up down clean

setup:
	cd backend && python -m venv .venv && $(PY_BACKEND) -m pip install -q -r requirements.txt pytest httpx ruff

run:
	cd backend && $(PY_BACKEND) -m uvicorn app.main:app --reload --port 8000

test:
	cd backend && $(PY_BACKEND) -m pytest -q

lint:
	cd backend && $(PY_BACKEND) -m ruff check .

up:
	cd infra && docker compose up -d --build

down:
	cd infra && docker compose down

clean:
	rm -rf backend/.venv backend/dev.db backend/.pytest_cache backend/.ruff_cache backend/app/__pycache__
