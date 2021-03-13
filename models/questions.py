from sqlalchemy import orm, String, Integer, Column, ForeignKey
from sqlalchemy_serializer import SerializerMixin

from __init__ import db


class Question(db.Model, SerializerMixin):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    author = Column(Integer, ForeignKey("users.id"))  # id автора
    header = Column(String, nullable=False)  # заголовок
    description = Column(String, nullable=False)  # описание
    user = orm.relation("User")  # связь с таблицой users
    answer = orm.relation("Answer")  # связь с таблицой answers
    categories = orm.relation("Category",  # ассоциативная связь с таблицой category
                              secondary="association",
                              backref="questions")
