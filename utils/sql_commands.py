from sqlalchemy import String
from sqlalchemy.exc import IntegrityError

from utils.datbase import session, get_session
from utils.schemas import User, Bans, Fire


def register_user(user_id: int, name: String, role: String):
    user = User(
        user_id=user_id,
        name=name,
        role=role
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def register_ban_user(user_id: int):
    user = Bans(
        user_id=user_id
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def delete_from_base(user_id: int, t):
    i = get_session().query(t).filter_by(user_id=user_id).delete()
    if i is None:
        return False
    get_session().commit()


def select_users():
    users = session.query(User).all()
    return users


def fire_to_sqlite(msg: String):
    message = Fire(
        msg=msg
    )
    session.add(message)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def get_fire_to_sqlite():
    info = get_session().query(Fire).distinct()
    shares = [x.msg for x in info]
    return shares[len(shares)-1]


def get_bans():
    info = get_session().query(Bans).distinct()
    shares = [x.user_id for x in info]
    return shares
