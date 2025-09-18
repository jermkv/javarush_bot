from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def info_inline():
    kb_list = [
        [InlineKeyboardButton(text='Состояние бота 🤖', callback_data='feeling_bot'),
         InlineKeyboardButton(text='Рассылка 📃', callback_data='text_send')],

        [InlineKeyboardButton(text='Моя Github', url='https://github.com/tamirlan1919')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard

def info_inline_second():
    kb_list = [
        [InlineKeyboardButton(text='1', callback_data='feeldfdfing_bot'),
         InlineKeyboardButton(text='2', callback_data='textfdf_send')],

        [InlineKeyboardButton(text='3', url='https://github.com/tamirlan1919')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard


def start_keyboard():
    kb_list = [
        [InlineKeyboardButton(text='🎲 Интересный факт', callback_data='random_fact')],
        [InlineKeyboardButton(text='🤖 ChatGPT', callback_data='chat_gpt')],
        [InlineKeyboardButton(text='👥 Общение с личностью', callback_data='random_fact')],
        [InlineKeyboardButton(text='🧠 Квиз', callback_data='qviz')],
        [InlineKeyboardButton(text='🌏 Переводчик', callback_data='translate')],
        [InlineKeyboardButton(text='🎥 Рекомендации', callback_data='recommendations')],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard


def fact_again_keyboard():
    kb_list = [
        [InlineKeyboardButton(text='🎯 Хочу еще факт', callback_data='random_fact')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard



