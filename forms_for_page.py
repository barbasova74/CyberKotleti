from flask_wtf import FlaskForm
from wtforms import (PasswordField, BooleanField, SubmitField, IntegerField, StringField, FileField,
                     widgets, SelectMultipleField, TextAreaField, FormField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Optional
from wtforms.form import BaseForm


class QuestionForm(FlaskForm):
    header = StringField('Заголовок', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class AnswerForm(FlaskForm):
    description = TextAreaField('Ответ', validators=[DataRequired()])
    submit = SubmitField('Отправить')
