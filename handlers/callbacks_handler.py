from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import fact_again_keyboard, get_persons_keyboard
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


@router.callback_query(F.data.startswith('quiz:'))
async def close_mode_handler(call: CallbackQuery, state: FSMContext):
    topic = call.data.split(':')[-1]

    # старт новой темы
    if topic in ['история', 'наука', 'it']:
        question = await get_quiz_question(topic)


        # сохраняем всё в dialogues
        dialogues[call.from_user.id] = {
            'topic': topic,
            'question': question,
            'score': None,
            'total': None
        }

        await call.message.answer(f'Тема: {topic}\n\n{question}')

        # FSM используем только для состояния "идёт квиз"
        await state.set_state(QuizStates.quiz_active)

        print(dialogues)


    # повторить квиз по той же теме
    elif topic == 'again':
        user_data = dialogues.get(call.from_user.id, {})
        saved_topic = user_data.get('topic')

        if not saved_topic:
            await call.message.answer("❗ Тема не найдена, начни квиз заново.")
            return

        question = await get_quiz_question(saved_topic)
        # сохраняем всё в dialogues
        dialogues[call.from_user.id] = {
            'topic': saved_topic,   # <-- исправлено
            'question': question,
            'score': None,
            'total': None
        }

        await call.message.answer(f'Тема: {saved_topic}\n\n{question}')
        await state.set_state(QuizStates.quiz_active)

        print(dialogues)




