from os import environ

import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()
__factory: orm.sessionmaker = None


def db_init(db_file):
    global __factory
    if __factory:
        return

    assert db_file.strip()

    conn_str = f"sqlite:///{db_file.strip()}?check_same_thread=False"
    engine = sa.create_engine(conn_str)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()


db_init(environ["DB_FILE"])
session = create_session()
