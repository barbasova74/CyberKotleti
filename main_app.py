from forms_for_page import *
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_restful import Api, abort
from werkzeug.utils import secure_filename
from requests import get, post, delete, put
from sqlite3 import connect
import requests
import os

con = connect("base.db", check_same_thread=False)
app = Flask(__name__)  # приложение
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'  # секретный ключ для csrf токена
app.config['UPLOAD_FOLDER'] = 'static\img\\'  # папка куда будут загружаться картинки пользователей
api = Api(app)


@app.route('/view_question/<int:qid>', methods=["GET", 'POST'])  # оработчик добавления работы
def view_question(qid):
    form = QuestionForm()  # форма
    answers = ()
    if request.method == "GET":
        cur = con.cursor()
        question = cur.execute(f"SELECT * FROM QUESTIONS WHERE id={qid}").fetchone()
        answers = cur.execute(f"SELECT * FROM ANSWERS WHERE qid={qid}").fetchall()
        print(question, answers)
        form.header.data = question[1]
        form.description.data = question[-1]
        con.commit()
    else:
        return redirect('/')  # возвращение на главную страницу
    return render_template('view_question.html', title='Question',  # отправляем на сервер шаблон
                           form=form, answers=answers)

@app.route('/add_question', methods=["GET", 'POST'])  # оработчик добавления работы
def add_question():
    form = QuestionForm()  # форма
    if form.validate_on_submit():  # если валидация прошла успешно(нет ошибок заполнения формы)
        cur = con.cursor()
        print(form.header.data)
        cur.execute(f"INSERT INTO QUESTIONS VALUES (?, ?)", (form.header.data, form.description.data))
        con.commit()
        return redirect('/')  # возвращение на главную страницу
    else:
        print(form.errors)  # если есть ошибки формы - показать
    return render_template('add_job_page.html', title='Adding question',  # отправляем на сервер шаблон
                           form=form)

@app.route('/', methods=['GET', 'POST'])   # обработчик главной страницы
def main_page():
    questions = ()
    if request.method == 'GET':
        cur = con.cursor()
        questions = cur.execute("SELECT * FROM QUESTIONS")
        con.commit()
    return render_template("questions_list.html", questions=questions, title="Main page")



def main():
    app.run(port=5050, debug=True)  # запуск приложения


if __name__ == '__main__':
    main()

