from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.recomendations import get_recommendations
from services.role_mode import ask_role_gpt

from keyboards.inline import close_mode, get_recommendation_action_keyboard, quiz_answers, topic_keyboard
from services.translator import translate_text
from states import Person, GPTDialog, MessageTalks, QuizStates, RecommendationStates, TranslationStates
from storage import dialogues
from services.quiz_service import check_answer
from .quiz_manager import increase_score, get_score

router = Router()


@router.message(MessageTalks.message)
async def message_handler(message: Message):
    answer = await ask_role_gpt(message.from_user.id, message.text)
    persona = dialogues[message.from_user.id]['persona']
    await message.answer(f'Answer - {answer}', reply_markup=close_mode())


@router.message(QuizStates.waiting_answer)
async def waiting_answer_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    question = data.get('question')
    result = await check_answer(question, message.text)
    await message.answer('Сейчас дам ответ')
    if result == 'правильно':
        score = await increase_score(state)
        await message.answer(f'✅ Правильно, твой счет {score}',reply_markup=quiz_answers())
    else:
        score = await get_score(state)
        await message.answer(f'⛔️ Неправильно твой счет {score}', reply_markup=quiz_answers())


@router.message(TranslationStates.waiting_text)
async def handle_translation_text(message: Message, state: FSMContext):
    data = await state.get_data()
    target_lang = data.get("target_lang", "en")
    text_to_translate = message.text

    translated = await translate_text(text_to_translate, target_lang)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сменить язык", callback_data="change_lang")],
        [InlineKeyboardButton(text="Закончить", callback_data="/start")]
    ])
    await message.answer(f"Перевод:\n{translated}", reply_markup=kb)

@router.message(RecommendationStates.choosing_genre)
async def recommendation_genre_chosen(message: Message, state: FSMContext):
    data = await state.get_data()
    rec_type = data.get("rec_type")
    genre = message.text

    await state.update_data(genre=genre)

    verb = {
        "books": "почитать",
        "movies": "посмотреть",
        "music": "послушать"
    }.get(rec_type)

    recommendations = await get_recommendations(rec_type, genre, [])
    await message.answer(
        f"Рекомендую {verb}:\n{recommendations}",
        reply_markup=get_recommendation_action_keyboard()
    )

    await state.set_state(RecommendationStates.showing_recommendation)
