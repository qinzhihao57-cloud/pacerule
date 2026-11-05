from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


def test_health_ok() -> None:
    with TestClient(app) as client:
        resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "db": "ok"}


def test_root_reports_version() -> None:
    with TestClient(app) as client:
        resp = client.get("/")
    body = resp.json()
    assert resp.status_code == 200
    assert body["name"]
    assert body["version"] == "0.1.0"


def test_openapi_available() -> None:
    with TestClient(app) as client:
        resp = client.get("/openapi.json")
    assert resp.status_code == 200
    assert "/health" in resp.json()["paths"]
