import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize("payload,expect", [
    ({"x": 2, "y": 3}, {"result": 5}),
    ({"x": "a", "y": 5}, {"error": "invalid_input"}),
])
def test_add_route(client, payload, expect):
    res = client.post("/add", json=payload)
    status = 400 if "error" in expect else 200
    assert res.status_code == status
    assert res.get_json() == expect


@pytest.mark.parametrize("payload,expect", [
    ({"x": 6, "y": 3}, {"result": 2}),
    ({"x": 1, "y": 0}, {"error": "division_by_zero"}),
    ({"x": "c", "y": 2}, {"error": "invalid_input"})
])
def test_divide_route(client, payload, expect):
    res = client.post("/divide", json=payload)
    status = 400 if "error" in expect else 200
    assert res.status_code == status
    assert res.get_json() == expect
