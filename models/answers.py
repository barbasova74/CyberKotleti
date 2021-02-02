from data.db_session import SqlAlchemyBase
from sqlalchemy import orm, String, Integer, ForeignKey, Column, DateTime
from sqlalchemy_serializer import SerializerMixin


class Answer(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    text = Column(String)
    qid = Column(Integer, ForeignKey("questions.id"))
    question = orm.relation("Question")  # связь с таблицой questions
