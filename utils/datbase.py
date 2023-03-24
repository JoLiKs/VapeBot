import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

engine = create_engine('sqlite:///base.db')
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
table = sqlalchemy.Table('users', sqlalchemy.MetaData(), autoload_with=engine)


def get_session():
    return session


def get_officers():
    info = get_session().query(table).filter_by(role="officer").distinct()
    shares = [x.user_id for x in info]
    return shares


def create_base():
    Base.metadata.create_all(engine)


def db_check(user_id):
    info = get_session().query(table).filter_by(user_id=user_id).first() is not None
    return info


def getNameById(user_id):
    info = session.query(table).filter_by(user_id=user_id).distinct()
    shares = [x.name for x in info]
    return shares[0]


def getIdByName(name):
    info = session.query(table).filter_by(name=name).distinct()
    shares = [x.user_id for x in info]
    if len(shares) == 0: return 0
    return shares[0]


def set_officerDB(username, t):
    i = get_session().query(t).filter_by(name=username).first()
    if i is None:
        return False
    i.role = 'officer'
    get_session().add(i)
    get_session().commit()
    return True


def del_officerDB(username, t):
    i = get_session().query(t).filter_by(name=username).first()
    if i is None:
        return False
    i.role = 'user'
    get_session().add(i)
    get_session().commit()
    return True


def get_users(t):
    i = get_session().query(t).distinct()
    shares = [x for x in i]
    if len(shares) == 0: return 0
    return shares
