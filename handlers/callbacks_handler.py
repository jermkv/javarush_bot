from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.quiz_manager import get_score
from keyboards.inline import fact_again_keyboard, topic_keyboard, start_keyboard, get_language_keyboard, \
    get_recommend_type_keyboard, get_recommendation_action_keyboard
from services.quiz_service import get_quiz_question
from services.random_fact import get_fact
from services.recomendations import get_recommendations
from storage import dialogues, PERSONS
from states import MessageTalks, QuizStates, TranslationStates, RecommendationStates

router = Router()


@router.callback_query(F.data == 'feeling_bot')
async def feel_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Привет')


@router.callback_query(F.data == 'text_send')
async def text_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Напиши текст для рассылки')


@router.callback_query(F.data == 'random_fact')
async def random_handler(call: CallbackQuery):
    await call.answer('Щас верну тебе рандомный факт', show_alert=True)
    fact = await get_fact()
    await call.message.answer(f'{fact}', reply_markup=fact_again_keyboard())



@router.callback_query(F.data.startswith('persona:'))
async def persona_handler(call: CallbackQuery, state: FSMContext):
    persona = call.data.split(':')[-1]

    #Инициализируем историю
    dialogues[call.from_user.id] = {
        'persona': PERSONS[persona],
        'messages': []
    }
    print(dialogues)
    await call.message.answer(f'Ты выбрал {persona}. Можешь пообщаться с ним')
    await state.set_state(MessageTalks.message)


@router.callback_query(F.data == 'close_mode')
async def close_mode_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()


@router.callback_query(F.data.startswith('topic:'))
async def close_mode_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    topic = call.data.split(':')[-1]
    question = await get_quiz_question(topic)
    await state.update_data(question=question)
    await state.update_data(topic=topic)
    await state.set_state(QuizStates.waiting_answer)
    await call.message.answer(f'Тема: {topic}\n\n{question}\nМожешь ответить на вопрос.')


@router.callback_query(F.data == 'next_question')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    data = await state.get_data()
    topic = data.get('topic')
    question = await get_quiz_question(topic)
    await call.message.answer(f'Продолжаем по теме: {topic}\n\n{question}')
    await state.set_state(QuizStates.waiting_answer)


@router.callback_query(F.data == 'change_topic')
async def next_quiz_question_handler(call: CallbackQuery):
    await call.message.answer('Выбери новую тему', reply_markup=topic_keyboard())


@router.callback_query(F.data == 'end_quiz')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    score = await get_score(state)
    await state.clear()
    await call.message.answer(f'🎬 Квиз завершен! Твйо итоговый счет: {score}')

@router.callback_query(F.data == "/start")
async def start_callback_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Выбери что-то', reply_markup=start_keyboard())
    await call.answer()

# ===== хендлеры для переводчика =====

@router.callback_query(F.data == "translate")
async def start_translation(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(TranslationStates.choosing_language)
    await call.message.answer(
        "Выберите язык для перевода:",
        reply_markup=get_language_keyboard()
    )
    await call.answer()


@router.callback_query(F.data.startswith("lang_"), TranslationStates.choosing_language)
async def language_chosen(call: CallbackQuery, state: FSMContext):
    lang_code = call.data.split("_")[1]
    await state.update_data(target_lang=lang_code)
    await state.set_state(TranslationStates.waiting_text)
    await call.message.answer("Отправьте текст, который нужно перевести.")
    await call.answer()


@router.callback_query(F.data == "change_lang", TranslationStates.waiting_text)
async def change_language(call: CallbackQuery, state: FSMContext):
    await state.set_state(TranslationStates.choosing_language)
    await call.message.answer(
        "Выберите язык для перевода:",
        reply_markup=get_language_keyboard()
    )
    await call.answer()

 # === recommendations ===

@router.callback_query(F.data == "recommendations")
async def recommendations_dialog_start(call: CallbackQuery, state: FSMContext):
    await state.set_state(RecommendationStates.choosing_type)
    await call.message.answer("Выберите категорию:", reply_markup=get_recommend_type_keyboard())
    await call.answer()

@router.callback_query(F.data.startswith("type_"), RecommendationStates.choosing_type)
async def recommendation_type_chosen(call: CallbackQuery, state: FSMContext):
    rec_type = call.data.split("_")[1]
    await state.update_data(rec_type=rec_type, not_liked=[])
    await state.set_state(RecommendationStates.choosing_genre)
    await call.message.answer("А какой жанр интересует? Напиши:")
    await call.answer()

@router.callback_query(F.data == "not_like", RecommendationStates.showing_recommendation)
async def recommendation_not_like(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    rec_type = data.get("rec_type")
    genre = data.get("genre")
    not_liked = data.get("not_liked", [])
    
    # Extract last recommended item from previous message (simple parse)
    last_recommendation = call.message.text.split("\n")[1] if "\n" in call.message.text else ""
    not_liked.append(last_recommendation)
    await state.update_data(not_liked=not_liked)
    recommendations = await get_recommendations(rec_type, genre, not_liked)
    await call.message.answer(f"Рекомендация:\n{recommendations}", reply_markup=get_recommendation_action_keyboard())
    await call.answer()