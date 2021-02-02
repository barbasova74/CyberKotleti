from data.db_session import SqlAlchemyBase
from sqlalchemy import orm, String, Integer, ForeignKey, Column, DateTime
from sqlalchemy_serializer import SerializerMixin


class Question(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    header = Column(String, nullable=False)  # заголовок
    description = Column(String, nullable=False)  # описание
    answer = orm.relation("Answer")  # связь с таблицой answers