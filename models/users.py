from data.db_session import SqlAlchemyBase
from sqlalchemy import orm, String, Integer, ForeignKey, Column
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)  # id
    surname = Column(String, nullable=False)  # фамилия
    name = Column(String, nullable=False)  # имя
    age = Column(Integer, nullable=False)  # возраст
    about = Column(String, nullable=True)  # описание
    login = Column(String, unique=True)  # почта - уникальна
