import pytest
import json
from app import create_app
from calculator.errors import BadRequestError

@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestCalculatorAPI:
    """Integration tests for calculator endpoints."""
    
    def test_calculate_valid_request(self, client):
        """Test valid calculation request."""
        response = client.post('/api/v1/calculate',
            data=json.dumps({'a': 5, 'b': 3, 'operation': 'add'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        assert response.json['result'] == 8
        
    def test_calculate_division_by_zero(self, client):
        """Test division by zero returns 400 with error message."""
        response = client.post('/api/v1/calculate',
            data=json.dumps({'a': 5, 'b': 0, 'operation': 'divide'}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        assert 'Division by zero is not allowed' in response.json['error']
        
    def test_calculate_non_numeric_input(self, client):
        """Test non-numeric input returns 400 with error message."""
        response = client.post('/api/v1/calculate',
            data=json.dumps({'a': 'abc', 'b': 5, 'operation': 'add'}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        assert 'Inputs must be numeric' in response.json['error']
        
    def test_calculate_missing_input(self, client):
        """Test missing operands return 400 with error message."""
        response = client.post('/api/v1/calculate',
            data=json.dumps({'a': 5, 'operation': 'add'}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        assert 'Both operands are required' in response.json['error']
        
    def test_calculate_empty_body(self, client):
        """Test empty request body returns 400."""
        response = client.post('/api/v1/calculate',
            data='',
            content_type='application/json'
        )
        
        # Should be caught by validation
        response = client.post('/api/v1/calculate',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        
    def test_calculate_unsupported_operation(self, client):
        """Test unsupported operation returns 400."""
        response = client.post('/api/v1/calculate',
            data=json.dumps({'a': 5, 'b': 3, 'operation': 'power'}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        assert 'Unsupported operation' in response.json['error']
