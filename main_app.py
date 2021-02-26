from forms_for_page import *
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_restful import Api, abort
from models.users import User
from models.answers import Answer
from models.questions import *
from data import db_session

from werkzeug.utils import secure_filename
from requests import get, post, delete, put
import requests
import os

app = Flask(__name__)  # приложение
app.config['SECRET_KEY'] = 'our_project_secret_key'  # секретный ключ для csrf токена
app.config['UPLOAD_FOLDER'] = 'static\img\\'  # папка куда будут загружаться картинки пользователей
db_session.global_init("db/helper_db.sqlite")  # создаем движок и подкление к бд


@app.route('/view_question/<int:qid>', methods=["GET", 'POST'])  # оработчик добавления работы
def view_question(qid):
    form = QuestionForm()  # форма
    session = db_session.create_session()
    question = session.query(Question).get(qid)
    answers = session.query(Answer).filter(Answer.qid == qid).all()
    print(answers)
    form.header.data = question.header
    form.description.data = question.description
    return render_template('view_question.html', title='Question', qid=qid,  # отправляем на сервер шаблон
                           form=form, answers=answers)

@app.route('/add_question', methods=["GET", 'POST'])  # оработчик добавления работы
def add_question():
    form = QuestionForm()  # форма
    if form.validate_on_submit():  # если валидация прошла успешно(нет ошибок заполнения формы)
        session = db_session.create_session()
        question = Question()
        question.header = form.header.data
        question.description = form.description.data
        session.add(question)
        session.commit()
        return redirect('/')  # возвращение на главную страницу
    else:
        print(form.errors)  # если есть ошибки формы - показать
    return render_template('add_question.html', title='Добавление вопроса',  # отправляем на сервер шаблон
                           form=form)

@app.route('/add_answer/<int:qid>', methods=["GET", 'POST'])  # оработчик добавления работы
def add_answer(qid):
    form = AnswerForm()  # форма
    if form.validate_on_submit():  # если валидация прошла успешно(нет ошибок заполнения формы)
        session = db_session.create_session()
        answer = Answer()
        answer.text = form.description.data
        answer.qid = qid
        session.add(answer)
        session.commit()
        return redirect('/')  # возвращение на главную страницу
    else:
        print(form.errors)  # если есть ошибки формы - показать
    return render_template('add_answer.html', title='Добавление ответа',  # отправляем на сервер шаблон
                           form=form)

@app.route('/', methods=['GET', 'POST'])   # обработчик главной страницы
def main_page():
    session = db_session.create_session()
    questions = session.query(Question)
    return render_template("questions_list.html", questions=questions, title="Главная страница")


