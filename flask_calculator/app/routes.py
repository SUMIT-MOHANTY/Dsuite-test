from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        operation = request.form.get('operation', 'add')
        
        result = 0
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({"success": False, "error": "Division by zero is not allowed"}), 400
            result = num1 / num2
        else:
            return jsonify({"success": False, "error": "Invalid operation"}), 400
            
        return jsonify({"success": True, "result": result})
    
    except ValueError as e:
        return jsonify({"success": False, "error": "Invalid input: please enter valid numbers"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
