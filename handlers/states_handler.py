from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from services.role_mode import ask_role_gpt

from keyboards.inline import close_mode, quiz_answers, topic_keyboard
from states import Person, GPTDialog, MessageTalks, QuizStates
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


