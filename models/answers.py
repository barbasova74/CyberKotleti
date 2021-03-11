from sqlalchemy import orm, String, Integer, ForeignKey, Column
from sqlalchemy_serializer import SerializerMixin

from __init__ import db


class Answer(db.Model, SerializerMixin):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    text = Column(String)
    qid = Column(Integer, ForeignKey("questions.id"))
    question = orm.relation("Question")  # связь с таблицой questions
