from flask import Blueprint, request, jsonify, render_template
from app.calculator import calculate
from app.forms import CalculationForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main_bp.route('/calculate', methods=['POST'])
def calculate_endpoint():
    form = CalculationForm()
    if form.validate_on_submit():
        result = calculate(form.num1.data, form.num2.data, form.operation.data)
        return jsonify(result), 200
    return jsonify({'success': False, 'error': 'Invalid form data'}), 400
