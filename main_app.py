from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user

from __init__ import app, login_manager
from forms_for_page import *
from models.answers import *
from models.categories import *
from models.questions import *
from models.users import *


@login_manager.user_loader
def load_user(user_id):  # функция получения авторизованного пользователя
    session = db.session()
    return session.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():  # выход из аккаунта
    logout_user()
    return redirect("/")


@app.route('/view_question/<int:qid>', methods=["GET", 'POST'])  # оработчик добавления работы
def view_question(qid):
    form = QuestionForm()  # форма
    session = db.session()
    question = session.query(Question).get(qid)
    answers = session.query(Answer).filter(Answer.qid == qid).all()
    print(answers)
    form.header.data = question.header
    form.description.data = question.description
    return render_template('view_question.html', title='Question', qid=qid,  # отправляем на сервер шаблон
                           form=form, answers=answers)


@app.route('/delete_question/<int:id>')  # обработчик удаления вопроса
@login_required
def delete_question(id):
    session = db.session()
    session.delete(session.query(Question).get(id))  # DELETE запрос на удаление работы
    session.commit()
    return redirect('/')


@app.route('/add_question', methods=["GET", 'POST'])  # оработчик добавления работы
def add_question():
    session = db.session()
    form = QuestionForm()  # форма
    choices = [(category.id - 1, category.name) for category in
               session.query(Category)]  # список кортежей: (значение, заголовок)
    form.select.choices = choices
    if form.validate_on_submit():  # если валидация прошла успешно(нет ошибок заполнения формы)

        question = Question()
        question.header = form.header.data
        question.description = form.description.data
        for category_name in [form.select.choices[val][1] for val in form.select.data]:
            category = session.query(Category).filter(Category.name == category_name).first()
            question.categories.append(category)
        if current_user.is_authenticated:
            question.user = current_user
        session.add(question)
        session.commit()
        return redirect(f'/view_question/{question.id}')  # возвращение на страницу вопроса
    else:
        print(form.errors)  # если есть ошибки формы - показать
    return render_template('add_question.html', title='Добавление вопроса',  # отправляем на сервер шаблон
                           form=form)


@app.route('/add_answer/<int:qid>', methods=["GET", 'POST'])  # оработчик добавления работы
def add_answer(qid):
    form = AnswerForm()  # форма
    if form.validate_on_submit():  # если валидация прошла успешно(нет ошибок заполнения формы)
        session = db.session()
        answer = Answer()
        answer.text = form.description.data
        answer.qid = qid
        session.add(answer)
        session.commit()
        return redirect(f'/view_question/{qid}')  # возвращение на главную страницу
    else:
        print(form.errors)  # если есть ошибки формы - показать
    return render_template('add_answer.html', title='Добавление ответа',  # отправляем на сервер шаблон
                           form=form)


@app.route('/login', methods=['GET', 'POST'])  # обработчик авторизации
def login():
    form = RegisterForm()  # форма
    if form.validate_on_submit():
        session = db.session()
        user = session.query(User).filter(
            User.login == form.login.data).first()  # ищем пользователя по введённой логину
        if user and user.check_password(
                form.password.data):  # если и логин и пароль подходят - авторизация пользователя
            login_user(user, remember=True)
            return redirect("/")
        return render_template('login_page.html',  # иначе тот же шаблон, с ошибкой
                               message="Неправильный логин или пароль", title='Авторизация',
                               form=form)
    return render_template('login_page.html', title='Aвторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])  # обработчик регистрации
def reqister():
    form = RegisterForm()  # форма
    if form.validate_on_submit():  # При успешной валидации отправляем данные и регистрируем пользователя
        session = db.session()
        if abort_if_user_login_equal_to_new_user_login(form.login.data):
            return render_template('register_page.html', title='Регистрация', form=form,
                                   message='Этот логин уже используется, придумайте другой')
        else:
            user = User()
            user.login = form.login.data
            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/')

    return render_template('register_page.html', title='Регистрация', form=form)


@app.route('/', methods=['GET', 'POST'])  # обработчик главной страницы
def main_page():
    session = db.session()
    questions = session.query(Question)
    return render_template("questions_list.html", questions=questions[::-1], title="Main page")


def main():
    app.run(debug=True)  # запуск приложения


def abort_if_user_login_equal_to_new_user_login(user_login):
    session = db.session()
    user = session.query(User).filter(User.login == user_login).first()
    return user


if __name__ == '__main__':
    main()
