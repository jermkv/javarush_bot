from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from storage import PERSONS

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
        [InlineKeyboardButton(text='👥 Общение с личностью', callback_data='talk')],
        [InlineKeyboardButton(text='🧠 Квиз', callback_data='qviz')],
        [InlineKeyboardButton(text='🌏 Переводчик', callback_data='translate')],
        [InlineKeyboardButton(text='🎥 Рекомендации', callback_data='recommendations')],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard


def fact_again_keyboard():
    kb_list = [
        [InlineKeyboardButton(text='Закончить', callback_data='/start'), InlineKeyboardButton(text='🎯 Хочу еще факт', callback_data='random_fact')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard


def get_persons_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f'persona:{name}')]
            for name in PERSONS
        ]
    )
    return kb


def close_mode():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Закончить', callback_data='/start')]
        ]
    )
    return kb


def topic_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='История', callback_data='topic:history')],
            [InlineKeyboardButton(text='Наука', callback_data='topic:science')],
            [InlineKeyboardButton(text='IT', callback_data='topic:it')],
        ]
    )
    return kb

def quiz_answers():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Еще вопрос', callback_data='next_question')],
            [InlineKeyboardButton(text='Сменить тему', callback_data='change_topic')],
            [InlineKeyboardButton(text='Закончить', callback_data='end_quiz')],
        ]
    )
    return kb

def get_language_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇫🇷 French", callback_data="lang_fr"),
        ],
        [
            InlineKeyboardButton(text="🇩🇪 German", callback_data="lang_de"),
            InlineKeyboardButton(text="🇪🇸 Spanish", callback_data="lang_es"),
        ]
    ])
    return kb

def get_recommend_type_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🎬 Фильмы", callback_data="type_movies"),
        ],
        [
            InlineKeyboardButton(text="📚 Книги", callback_data="type_books"),
        ],
        [
            InlineKeyboardButton(text="🎵 Музыка", callback_data="type_music"),
        ],
    ])
    return kb

def get_recommendation_action_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Не нравится", callback_data="not_like")],
        [InlineKeyboardButton(text="Закончить", callback_data="/start")]
    ])
    return kb

# Create "Назад" button
def get_back_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="/start")]
        ]
    )
    return kb