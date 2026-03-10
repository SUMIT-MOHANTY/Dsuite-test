import math

from calculator.errors import BadRequestError

def calculate(a: float, b: float, operation: str) -> float:
    """
    Perform calculation with input validation.
    
    Args:
        a: First operand
        b: Second operand  
        operation: Arithmetic operation (add, subtract, multiply, divide)
        
    Returns:
        float: Calculation result
        
    Raises:
        BadRequestError: For invalid inputs or division by zero
    """
    # Check for missing/None inputs
    if a is None or b is None:
        raise BadRequestError("Both operands are required.")
    
    # Validate numeric inputs
    try:
        a_num = float(a)
        b_num = float(b)
    except (TypeError, ValueError):
        raise BadRequestError("Inputs must be numeric.")
    
    operation = operation.lower()
    
    if operation == "add":
        return a_num + b_num
    elif operation == "subtract":
        return a_num - b_num
    elif operation == "multiply":
        return a_num * b_num
    elif operation == "divide":
        # Check for division by zero (with tolerance for floating point)
        if abs(b_num) < 1e-10:
            raise BadRequestError("Division by zero is not allowed.")
        return a_num / b_num
    else:
        raise BadRequestError("Unsupported operation.")
