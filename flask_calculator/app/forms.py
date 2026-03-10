from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import DataRequired, NumberRange

class CalculatorForm(FlaskForm):
    """Form for calculator input validation."""
    num1 = FloatField('num1', validators=[
        DataRequired(message="First number is required"),
    ])
    num2 = FloatField('num2', validators=[
        DataRequired(message="Second number is required"),
    ])
    operation = StringField('operation', validators=[
        DataRequired(message="Operation is required")
    ])
    
    def validate_operation(self, field):
        """Custom validation for operation field."""
        if field.data not in ['add', 'subtract', 'multiply', 'divide']:
            raise ValueError("Invalid operation. Must be add, subtract, multiply, or divide")
