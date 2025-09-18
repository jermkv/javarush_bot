from aiogram.fsm.state import State, StatesGroup


class Person(StatesGroup):
    name = State()
    age = State()
    city = State()

