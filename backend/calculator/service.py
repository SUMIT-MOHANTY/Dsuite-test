from typing import Dict, Any
from calculator.errors import ValidationError, DivisionByZeroError

class CalculatorService:
    def calculate(self, a: float, b: float, operation: str) -> float:
        if not isinstance(operation, str):
            raise ValidationError("Operation must be a string")
        
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                raise DivisionByZeroError("Cannot divide by zero")
            return a / b
        else:
            raise ValidationError(f"Unsupported operation: {operation}")
