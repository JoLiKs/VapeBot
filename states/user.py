from aiogram.dispatcher.filters.state import StatesGroup, State


class Mail(StatesGroup):
    mail = State()
    name = State()

class Name(StatesGroup):
    builder = State()
    join = State()
    name = State()
    planet = State()
    countEnemy = State()


class Admin(StatesGroup):
    officer = State()
    officer_del = State()