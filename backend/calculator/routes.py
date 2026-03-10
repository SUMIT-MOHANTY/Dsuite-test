from flask import Blueprint, request, jsonify
from calculator.service import CalculatorService
from calculator.errors import CalculatorError

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        a = data.get('a')
        b = data.get('b')
        operation = data.get('operation')
        
        if a is None or b is None or operation is None:
            return jsonify({"error": "Missing required fields"}), 400
        
        service = CalculatorService()
        result = service.calculate(float(a), float(b), operation)
        
        return jsonify({"result": result}), 200
        
    except CalculatorError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500
