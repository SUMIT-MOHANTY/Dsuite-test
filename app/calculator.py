def perform_add(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("invalid_input")
    return float(x + y)


def perform_divide(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("invalid_input")
    if y == 0:
        raise ValueError("division_by_zero")
    return float(x / y)
