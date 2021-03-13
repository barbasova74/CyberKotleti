from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, widgets, SelectMultipleField, TextAreaField)
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()


class QuestionForm(FlaskForm):
    header = StringField('', validators=[DataRequired()])
    description = TextAreaField('Попросите оставить отвечающих контакты, если вы хотите с ними связаться',
                                validators=[DataRequired()])
    select = MultiCheckboxField("Label", coerce=int)
    submit = SubmitField('Опубликовать')


class AnswerForm(FlaskForm):
    description = TextAreaField('Оставьте ваши контакты, если вы хотите объяснить тему лично или более наглядно',
                                validators=[DataRequired()])
    submit = SubmitField('Опубликовать')


class RegisterForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
