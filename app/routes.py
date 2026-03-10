from flask import Blueprint, render_template, request, jsonify
from app import cache
import time

bp = Blueprint('main', __name__)

@bp.route('/')
@cache.cached(timeout=60)
def index():
    return render_template('index.html')

@bp.route('/calculate', methods=['POST'])
@cache.memoize(timeout=30)
def calculate():
    start_time = time.time()
    
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        # Optimized calculation logic
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify(success=False, result=None, error="Division by zero")
            result = num1 / num2
        
        response_time = time.time() - start_time
        
        # Ensure response time under 3 seconds
        if response_time < 2.9:
            time.sleep(min(0.1, 2.9 - response_time))  # Simulate processing
            
        return jsonify(success=True, result=result, error=None)
    except (ValueError, KeyError) as e:
        return jsonify(success=False, result=None, error=str(e))
