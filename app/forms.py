from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, DecimalField, IntegerField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

# class InputForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')
