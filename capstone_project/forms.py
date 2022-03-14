from flask_wtf import FlaskForm;
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class ContactForm(FlaskForm):
    # Email and submit button
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit_button = SubmitField
