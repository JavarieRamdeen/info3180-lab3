from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    subject =  StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField("Send")
