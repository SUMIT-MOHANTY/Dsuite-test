import pytest
import math
from calculator.service import calculate
from calculator.errors import BadRequestError

class TestCalculateService:
    """Test the calculation service with various inputs."""
    
    def test_add_valid_inputs(self):
        """Test addition with valid inputs."""
        assert abs(calculate(2, 3, "add") - 5) < 1e-10
        
    def test_subtract_valid_inputs(self):
        """Test subtraction with valid inputs."""
        assert abs(calculate(5, 3, "subtract") - 2) < 1e-10
        
    def test_multiply_valid_inputs(self):
        """Test multiplication with valid inputs."""
        assert abs(calculate(4, 3, "multiply") - 12) < 1e-10
        
    def test_divide_valid_inputs(self):
        """Test division with valid inputs."""
        assert abs(calculate(10, 2, "divide") - 5) < 1e-10
    
    def test_divide_by_zero(self):
        """Test division by zero raises BadRequestError."""
        with pytest.raises(BadRequestError, match="Division by zero is not allowed"):
            calculate(5, 0, "divide")
    
    def test_non_numeric_inputs(self):
        """Test non-numeric inputs raise BadRequestError."""
        with pytest.raises(BadRequestError, match="Inputs must be numeric"):
            calculate("abc", 5, "add")
        
        with pytest.raises(BadRequestError, match="Inputs must be numeric"):
            calculate(5, "xyz", "multiply")
    
    def test_null_inputs(self):
        """Test null/None inputs raise BadRequestError."""
        with pytest.raises(BadRequestError, match="Both operands are required"):
            calculate(None, 5, "add")
            
        with pytest.raises(BadRequestError, match="Both operands are required"):
            calculate(5, None, "add")
    
    def test_unsupported_operation(self):
        """Test unsupported operation raises BadRequestError."""
        with pytest.raises(BadRequestError, match="Unsupported operation"):
            calculate(5, 3, "power")
            
    def test_case_insensitive_operation(self):
        """Test operations are case insensitive."""
        assert abs(calculate(2, 3, "ADD") - 5) < 1e-10
        assert abs(calculate(2, 3, "Add") - 5) < 1e-10
