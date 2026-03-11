import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_add_success(client):
    response = client.post('/add', json={'x': 2, 'y': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_add_invalid_input(client):
    response = client.post('/add', json={'x': 'a', 'y': 3})
    assert response.status_code == 400
    assert response.json['error'] == 'invalid_input'

def test_divide_success(client):
    response = client.post('/divide', json={'x': 6, 'y': 2})
    assert response.status_code == 200
    assert response.json['result'] == 3

def test_divide_by_zero(client):
    response = client.post('/divide', json={'x': 5, 'y': 0})
    assert response.status_code == 400
    assert response.json['error'] == 'division_by_zero'
