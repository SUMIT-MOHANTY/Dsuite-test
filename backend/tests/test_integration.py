"""
Integration tests for calculator API.
"""

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestCalculatorAPI:
    def test_add_endpoint(self, client):
        response = client.post('/api/v1/calculate', json={
            'a': 5, 'b': 3, 'operation': 'add'
        })
        assert response.status_code == 200
        assert response.json == {'result': 8}
    
    def test_invalid_operation(self, client):
        response = client.post('/api/v1/calculate', json={
            'a': 5, 'b': 3, 'operation': 'invalid'
        })
        assert response.status_code == 422
    
    def test_division_by_zero(self, client):
        response = client.post('/api/v1/calculate', json={
            'a': 5, 'b': 0, 'operation': 'divide'
        })
        assert response.status_code == 400
        assert 'error' in response.json
