def calculate(num1, num2, operation):
    """Perform calculation based on operation"""
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return {'success': False, 'error': 'Cannot divide by zero', 'result': None}
            result = num1 / num2
        else:
            return {'success': False, 'error': 'Invalid operation', 'result': None}
            
        return {'success': True, 'result': result, 'error': None}
    except (ValueError, TypeError):
        return {'success': False, 'error': 'Invalid numbers provided', 'result': None}
