import pytest
from app.calculator import perform_add, perform_divide

def test_add():
    assert perform_add(2, 3) == 5
    assert perform_add(-1, 1) == 0
    assert perform_add(0.5, 0.5) == 1.0

def test_divide():
    assert perform_divide(6, 2) == 3
    assert perform_divide(1, 1) == 1
    assert perform_divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="division_by_zero"):
        perform_divide(5, 0)
