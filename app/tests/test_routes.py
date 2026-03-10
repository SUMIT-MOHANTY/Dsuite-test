import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_calculate_addition(client):
    rv = client.post('/calculate', data={'num1': 5, 'num2': 3, 'operation': 'add'})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['success'] is True
    assert data['result'] == 8.0
