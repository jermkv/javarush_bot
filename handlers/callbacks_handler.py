from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.quiz_manager import get_score
from keyboards.inline import fact_again_keyboard, topic_keyboard
from services.quiz_service import get_quiz_question
from services.random_fact import get_fact
from storage import dialogues, PERSONS
from states import MessageTalks, QuizStates


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