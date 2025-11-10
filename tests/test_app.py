import json
from app.app import app

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert json.loads(r.data.decode())["status"] == "ok"

def test_api_top_returns_rows():
    client = app.test_client()
    r = client.get("/api/top?limit=3")
    assert r.status_code == 200
    rows = json.loads(r.data.decode())
    assert len(rows) == 3
    assert "symbol" in rows[0]
    assert "dividend_yield" in rows[0]
