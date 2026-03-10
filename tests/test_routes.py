import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Secure Calculator' in response.data

def test_calculate_valid_addition(client):
    response = client.post('/calculate', data={
        'num1': 5,
        'num2': 3,
        'operation': 'add'
    })
    assert response.json['success'] is True
    assert response.json['result'] == 8.0

def test_calculate_division_by_zero(client):
    response = client.post('/calculate', data={
        'num1': 5,
        'num2': 0,
        'operation': 'divide'
    })
    assert response.json['success'] is False
    assert 'Cannot divide by zero' in response.json['error']
