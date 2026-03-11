def perform_add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

def perform_divide(x: float, y: float) -> float:
    """Divide two numbers."""
    if y == 0:
        raise ValueError("division_by_zero")
    return x / y
