from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField

class CalculationForm(FlaskForm):
    item1 = SelectField(choices=[('apple', 'Apple'), ('orange', 'Orange'),
                                   ('banana', 'Banana')])
    item2 = SelectField(choices=[('apple', 'Apple'), ('orange', 'Orange'),
                                   ('banana', 'Banana')])
    quantity1 = IntegerField()

    submit = SubmitField('Submit')
