from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
    kb_lsit = [
        [KeyboardButton(text='С пюрешкой 🥔'), KeyboardButton(text='С макарошками 🍝')],
        [KeyboardButton(text='С гречкой 🌾')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_lsit, resize_keyboard=True)
    return keyboard