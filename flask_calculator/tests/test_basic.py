import pytest
from app.calculator import perform_add, perform_divide

def test_add():
    assert perform_add(3, 4) == 7
    assert perform_add(-3, 4) == 1
    assert perform_add(0, 0) == 0

def test_divide():
    assert perform_divide(10, 2) == 5
    assert perform_divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="division_by_zero"):
        perform_divide(5, 0)
