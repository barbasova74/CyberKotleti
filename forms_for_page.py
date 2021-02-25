from flask_wtf import FlaskForm
from wtforms import (PasswordField, BooleanField, SubmitField, IntegerField, StringField, FileField,
                     widgets, SelectMultipleField, TextAreaField, FormField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Optional
from wtforms.form import BaseForm


class QuestionForm(FlaskForm):
    header = StringField('', validators=[DataRequired()])
    description = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')

class AnswerForm(FlaskForm):
    description = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
