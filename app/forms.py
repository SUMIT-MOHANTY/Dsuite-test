from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class CalculationForm(FlaskForm):
    num1 = FloatField('Number 1', validators=[DataRequired(), NumberRange()])
    num2 = FloatField('Number 2', validators=[DataRequired(), NumberRange()])
    operation = SelectField('Operation', choices=[
        ('add', 'Addition'),
        ('subtract', 'Subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division')
    ], validators=[DataRequired()])
