import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
from messages.start_text import TEXT
from keyboards.reply import start_keyboard
from keyboards.inline import info_inline
import logging


bot = Bot(TOKEN) #Связывались с серверами тг с нашим токеном
dp = Dispatcher() #Ловит апдейты


@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(TEXT)
    await message.answer(f'Привет еще {message.from_user.full_name}')


@dp.message(Command('info'))
async def info_handler(message: Message):
    await message.answer('Можешь ознакомиться с панелью', reply_markup=info_inline())




@dp.message(F.text.lower() == 'привет')
async def text_handler(message: Message):
    await message.answer('И тебе привет мой друг 👋')


@dp.message(F.text.lower() == 'пока')
async def text_handler(message: Message):
    await message.answer('Очень жаль что ты уходишь(')

@dp.message(F.text.lower() == 'файл')
async def file_handler(message: Message):
    doc = FSInputFile('lesson.pdf')
    await message.answer_document(doc)

@dp.message(F.text.lower() == 'еда')
async def eat_handelr(message: Message):
    await message.answer('Как будешь кушать катлетки?', reply_markup=start_keyboard())




@dp.message(F.text.lower().contains('как дела'))
async def text_handler(message: Message):
    await message.answer('Все отлично')

@dp.message(F.text == 'С пюрешкой 🥔')
async def potato_handler(message: Message):
    await message.answer('Отличный выбор')

@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer('Это фотка вот тебе ответка')
    img = FSInputFile('media/img/code.png')
    await message.answer_photo(img)




@dp.message(F.voice)
async def photo_handler(message: Message):
    await message.answer('Это гс')

@dp.message(F.sticker)
async def photo_handler(message: Message):
    await message.answer('Это стикер')




async def main():
    logging.basicConfig(level=logging.INFO) #Логирование
    await dp.start_polling(bot)


asyncio.run(main())

