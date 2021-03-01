from flask_wtf import FlaskForm
from wtforms import (PasswordField, BooleanField, SubmitField, IntegerField, StringField, FileField,
                     widgets, SelectMultipleField, TextAreaField, FormField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Optional
from wtforms.form import BaseForm


class QuestionForm(FlaskForm):
    header = StringField('', validators=[DataRequired()])
    description = TextAreaField('Попросите оставить отвечающих контакты, если вы хотите с ними связаться', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')

class AnswerForm(FlaskForm):
    description = TextAreaField('Оставьте ваши контакты, если вы хотите объяснить тему лично или более наглядно', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')

class RegisterForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')