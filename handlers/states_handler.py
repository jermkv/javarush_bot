from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.quiz_service import check_answer
from services.role_mode import ask_role_gpt

from keyboards.inline import close_mode, quiz_answers
from states import Person, GPTDialog, MessageTalks, QuizStates
from storage import dialogues

router = Router()


@router.message(MessageTalks.message)
async def message_handler(message: Message):
    answer = await ask_role_gpt(message.from_user.id, message.text)
    persona = dialogues[message.from_user.id]['persona']
    await message.answer(f'Answer - {answer}', reply_markup=close_mode())


@router.message(QuizStates.quiz_active)
async def answer_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_answer = message.text
    question = dialogues[user_id].get('question')

    if not question:
        await message.answer("Нет активного вопроса. Начни квиз сначала.")
        return

    result = await check_answer(question, user_answer)

    await message.answer(result, reply_markup=quiz_answers())

    # Optionally clear state or move to next question
    await state.clear()
