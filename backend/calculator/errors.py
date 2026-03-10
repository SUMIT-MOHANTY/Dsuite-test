"""
Centralized error handling for calculator service.
"""

class CalculationError(Exception):
    """Base exception for calculation errors."""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ValidationError(CalculationError):
    """Raised when input validation fails."""
    pass

class DivisionByZeroError(CalculationError):
    """Raised when attempting to divide by zero."""
    def __init__(self):
        super().__init__("Cannot divide by zero", 400)
