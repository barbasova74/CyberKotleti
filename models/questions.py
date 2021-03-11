from sqlalchemy import orm, String, Integer, Column
from sqlalchemy_serializer import SerializerMixin

from __init__ import db


class Question(db.Model, SerializerMixin):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    header = Column(String, nullable=False)  # заголовок
    description = Column(String, nullable=False)  # описание
    answer = orm.relation("Answer")  # связь с таблицой answers
