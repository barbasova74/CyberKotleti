from sqlalchemy import String, Integer, ForeignKey, Column, Table
from sqlalchemy_serializer import SerializerMixin

from __init__ import db

association_table = Table('association', db.Model.metadata,  # промежуточная таблица категорий работ
                          Column('question', Integer,
                                 ForeignKey('questions.id')),
                          Column('category', Integer,
                                 ForeignKey('category.id'))
                          )


class Category(db.Model, SerializerMixin):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True,  # id
                autoincrement=True)
    name = Column(String, nullable=False)  # наименование категории
