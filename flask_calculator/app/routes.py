from flask import Blueprint, request, jsonify
from .calculator import perform_add, perform_divide

bp = Blueprint('calculator', __name__)

@bp.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    try:
        x = float(data['x'])
        y = float(data['y'])
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'invalid_input'}), 400
    
    try:
        result = perform_add(x, y)
    except Exception:
        return jsonify({'error': 'invalid_input'}), 400
    
    return jsonify({'result': result})

@bp.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    try:
        x = float(data['x'])
        y = float(data['y'])
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'invalid_input'}), 400
    
    try:
        result = perform_divide(x, y)
    except ValueError as e:
        if str(e) == "division_by_zero":
            return jsonify({'error': 'division_by_zero'}), 400
        return jsonify({'error': 'invalid_input'}), 400
    
    return jsonify({'result': result})
