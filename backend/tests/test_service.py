import pytest
from calculator.service import CalculatorService
from calculator.errors import ValidationError, DivisionByZeroError

@pytest.fixture
def service():
    return CalculatorService()

def test_add(service):
    assert service.calculate(2, 3, "add") == 5

def test_subtract(service):
    assert service.calculate(5, 3, "subtract") == 2

def test_multiply(service):
    assert service.calculate(4, 3, "multiply") == 12

def test_divide(service):
    assert service.calculate(6, 2, "divide") == 3

def test_divide_by_zero(service):
    with pytest.raises(DivisionByZeroError):
        service.calculate(6, 0, "divide")

def test_invalid_operation(service):
    with pytest.raises(ValidationError):
        service.calculate(6, 2, "invalid")
