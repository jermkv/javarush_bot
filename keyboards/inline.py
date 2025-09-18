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



