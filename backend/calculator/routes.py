from flask import Blueprint, request, jsonify
from calculator.service import calculate
from calculator.errors import BadRequestError

calculator_bp = Blueprint('calculator', __name__, url_prefix='/api/v1')

@calculator_bp.route('/calculate', methods=['POST'])
def calculate_endpoint():
    """Endpoint for performing calculations."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    try:
        a = data.get('a')
        b = data.get('b')
        operation = data.get('operation')
        
        result = calculate(a, b, operation)
        return jsonify({'result': result}), 200
        
    except BadRequestError as e:
        return jsonify({'error': str(e)}), 400
