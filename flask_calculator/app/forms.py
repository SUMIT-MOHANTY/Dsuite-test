# Placeholder for future form validation classes
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    num1 = FloatField('First Number', validators=[DataRequired()])
    num2 = FloatField('Second Number', validators=[DataRequired()])
    operation = StringField('Operation', validators=[DataRequired()])
