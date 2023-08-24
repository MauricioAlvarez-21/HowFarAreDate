from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class InputDatesForm(FlaskForm):
    date1=DateField('Input Date 1', validators=[DataRequired()])
    date2=DateField('Input Date 2', validators=[DataRequired()])
    submit = SubmitField('Submit')