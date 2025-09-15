from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def info_inline():
    kb_list = [
        [InlineKeyboardButton(text='Состояние бота 🤖', callback_data='feeling_bot'),
         InlineKeyboardButton(text='Рассылка 📃', callback_data='text_send')],

        [InlineKeyboardButton(text='Моя Github', url='https://github.com/tamirlan1919')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard


