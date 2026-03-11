def perform_add(x, y):
    return x + y

def perform_divide(x, y):
    if y == 0:
        raise ZeroDivisionError("division_by_zero")
    return x / y
