from fastapi.testclient import TestClient
from devvault.api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_search_endpoint_no_results():
    response = client.get("/search", params={"q": "somethingveryunlikely12345"})
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "somethingveryunlikely12345"
    assert data["results"] == []