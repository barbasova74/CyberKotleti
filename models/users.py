from data.db_session import SqlAlchemyBase
from sqlalchemy import orm, String, Integer, ForeignKey, Column
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    login = Column(String, unique=True)
    password = Column(String, nullable=False)

    def set_password(self, password):  # захешировать пароль
        self.password = generate_password_hash(password)

    def check_password(self, password):  # сверить пароль
        return check_password_hash(self.password, password)
