"""
Unit tests for calculator service.
"""

import pytest
from calculator.service import CalculatorService
from calculator.errors import DivisionByZeroError

class TestCalculatorService:
    def test_add(self):
        service = CalculatorService()
        assert service.add(2, 3) == 5
        assert service.add(-1, 1) == 0
    
    def test_subtract(self):
        service = CalculatorService()
        assert service.subtract(5, 3) == 2
        assert service.subtract(1, 1) == 0
    
    def test_multiply(self):
        service = CalculatorService()
        assert service.multiply(3, 4) == 12
        assert service.multiply(-2, 5) == -10
    
    def test_divide(self):
        service = CalculatorService()
        assert service.divide(10, 2) == 5
        assert service.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        service = CalculatorService()
        with pytest.raises(DivisionByZeroError):
            service.divide(5, 0)
