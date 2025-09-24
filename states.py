from aiogram.fsm.state import State, StatesGroup


class Person(StatesGroup):
    name = State()
    age = State()
    city = State()


class GPTDialog(StatesGroup):
    message = State()


class MessageTalks(StatesGroup):
    message = State()

class QuizStates(StatesGroup):
    quiz_active = State()
    topic = State()