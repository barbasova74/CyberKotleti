import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import os


SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory
    
    if __factory:
        return
    print(__factory)
    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = os.environ.get('DATABASE_URL', 'sqlite:///db/helper_db.sqlite?check_same_thread=False')
    print(f"Подключение к базе данных по адресу {conn_str}")
    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from data import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    print(__factory)
    return __factory()
