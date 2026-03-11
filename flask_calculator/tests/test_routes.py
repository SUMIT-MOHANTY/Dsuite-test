import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_endpoint(client):
    res = client.post("/add", json={"x": 2, "y": 3})
    assert res.status_code == 200
    assert res.json["result"] == 5

    res = client.post("/add", json={"x": "a", "y": 3})
    assert res.status_code == 400
    assert res.json["error"] == "invalid_input"

def test_divide_endpoint(client):
    res = client.post("/divide", json={"x": 6, "y": 2})
    assert res.status_code == 200
    assert res.json["result"] == 3

    res = client.post("/divide", json={"x": 5, "y": 0})
    assert res.status_code == 400
    assert res.json["error"] == "division_by_zero"

    res = client.post("/divide", json={"x": "x", "y": 1})
    assert res.status_code == 400
    assert res.json["error"] == "invalid_input"
