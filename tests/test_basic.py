import pytest
from app.calculator import perform_add, perform_divide


@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2.0)
])
def test_add_valid(x, y, expected):
    assert perform_add(x, y) == expected


@pytest.mark.parametrize("x,y", [
    ("a", 1), (None, 5), (2, {})
])
def test_add_invalid(x, y):
    with pytest.raises(TypeError):
        perform_add(x, y)


@pytest.mark.parametrize("x,y,expected", [
    (6, 3, 2.0),
    (-4, 2, -2.0),
    (5, 2, 2.5)
])
def test_divide_valid(x, y, expected):
    assert perform_divide(x, y) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        perform_divide(1, 0)


@pytest.mark.parametrize("x,y", [("a", 1), (1, "b")])
def test_divide_invalid(x, y):
    with pytest.raises(TypeError):
        perform_divide(x, y)
