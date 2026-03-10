from flask import Blueprint, render_template, request, jsonify
from app.forms import CalculatorForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Serve the calculator template."""
    return render_template('index.html')

@bp.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculator form submission."""
    form = CalculatorForm()
    
    if not form.validate_on_submit():
        return jsonify({
            "success": False,
            "result": None,
            "error": "Invalid input data"
        }), 400
    
    num1 = form.num1.data
    num2 = form.num2.data
    operation = form.operation.data
    
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({
                    "success": False,
                    "result": None,
                    "error": "Cannot divide by zero"
                }), 400
            result = num1 / num2
        else:
            return jsonify({
                "success": False,
                "result": None,
                "error": "Invalid operation"
            }), 400
        
        return jsonify({
            "success": True,
            "result": result,
            "error": None
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "result": None,
            "error": str(e)
        }), 500
