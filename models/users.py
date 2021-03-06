from flask_login import UserMixin
from sqlalchemy import orm, String, Integer, Column
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from __init__ import db


class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    login = Column(String, unique=True)
    password = Column(String, nullable=False)
    job = orm.relation("Question", back_populates='user')

    def set_password(self, password):  # захешировать пароль
        self.password = generate_password_hash(password)

    def check_password(self, password):  # сверить пароль
        return check_password_hash(self.password, password)
