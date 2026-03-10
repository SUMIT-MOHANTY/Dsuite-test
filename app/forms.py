from wtforms import Form, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class CalculatorForm(Form):
    num1 = FloatField('Number 1', validators=[DataRequired(), NumberRange(min=-1e308, max=1e308)])
    num2 = FloatField('Number 2', validators=[DataRequired(), NumberRange(min=-1e308, max=1e308)])
    operation = SelectField('Operation', choices=[
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide')
    ], validators=[DataRequired()])
