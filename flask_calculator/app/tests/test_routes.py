import pytest
from app import create_app

@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that index route returns 200."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_calculate_add(client):
    """Test addition via POST to /calculate."""
    rv = client.post('/calculate', data={
        'num1': '5',
        'num2': '3',
        'operation': 'add'
    })
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['success'] is True
    assert json_data['result'] == 8

def test_calculate_divide_by_zero(client):
    """Test divide by zero handling."""
    rv = client.post('/calculate', data={
        'num1': '5',
        'num2': '0',
        'operation': 'divide'
    })
    json_data = rv.get_json()
    assert rv.status_code == 400
    assert json_data['success'] is False
    assert 'divide by zero' in json_data['error']
