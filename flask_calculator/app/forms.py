from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class CalculatorForm(FlaskForm):
    num1 = FloatField('First Number', validators=[DataRequired(), NumberRange()])
    num2 = FloatField('Second Number', validators=[DataRequired(), NumberRange()])
    operation = SelectField('Operation', choices=[
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide')
    ], validators=[DataRequired()])
