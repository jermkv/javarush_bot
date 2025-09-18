from aiogram import Router, F
from aiogram.types import FSInputFile, Message

from keyboards.reply import start_keyboard

router = Router()


@router.message(F.text.lower() == 'привет')
async def text_handler(message: Message):
    await message.answer('И тебе привет мой друг 👋')


@router.message(F.text.lower() == 'пока')
async def text_handler(message: Message):
    await message.answer('Очень жаль что ты уходишь(')


@router.message(F.text.lower() == 'файл')
async def file_handler(message: Message):
    doc = FSInputFile('lesson.pdf')
    await message.answer_document(doc)


@router.message(F.text.lower() == 'еда')
async def eat_handelr(message: Message):
    await message.answer('Как будешь кушать катлетки?', reply_markup=start_keyboard())


@router.message(F.text.lower().contains('как дела'))
async def text_handler(message: Message):
    await message.answer('Все отлично')


@router.message(F.text == 'С пюрешкой 🥔')
async def potato_handler(message: Message):
    await message.answer('Отличный выбор')
