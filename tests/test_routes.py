from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_default():
    response = client.get("/")
    assert response.status_code == 204

def test_hostname():
    response = client.get("/hostname")
    assert response.status_code == 200
    assert list(response.json().keys())[0] == "hostname"

def test_not_found():
    response = client.get("/notfound")
    assert response.status_code == 404
