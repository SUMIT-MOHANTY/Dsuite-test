class CalculatorError(Exception):
    pass

class ValidationError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass
