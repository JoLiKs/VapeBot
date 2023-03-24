from sqlalchemy import Column, Integer, String

from utils.datbase import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    name = Column(String, unique=True)
    role = Column(String, unique=False)


class Bans(Base):
    __tablename__ = 'bans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)


class Fire(Base):
    __tablename__ = 'fire'

    id = Column(Integer, primary_key=True)
    msg = Column(String, unique=False)
