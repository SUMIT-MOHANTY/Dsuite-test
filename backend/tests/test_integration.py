import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_add(client):
    response = client.post('/api/v1/calculate', json={
        'a': 2,
        'b': 3,
        'operation': 'add'
    })
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_calculate_divide_zero(client):
    response = client.post('/api/v1/calculate', json={
        'a': 5,
        'b': 0,
        'operation': 'divide'
    })
    assert response.status_code == 400
    assert 'error' in response.json

def test_calculate_missing_fields(client):
    response = client.post('/api/v1/calculate', json={})
    assert response.status_code == 400
    assert 'error' in response.json
