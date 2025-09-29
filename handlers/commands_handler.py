from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.dialog_gpt import dialog_gpt_func
from states import Person, GPTDialog
from services.random_fact import get_fact
from keyboards.inline import start_keyboard, get_persons_keyboard, topic_keyboard, get_back_keyboard
from storage import dialogues

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Выбери что-то', reply_markup=start_keyboard())


@router.message(Person.name)
async def name_handler(message: Message, state: FSMContext):
    await message.answer(f'Окей {message.text} а сколько тебе лет? ')
    await state.update_data(name=message.text)
    await state.set_state(Person.age)


@router.message(Person.age)
async def age_handler(message: Message, state: FSMContext):
    await message.answer(f'Тебе {message.text} , откуда ты? ')
    await state.update_data(age=message.text)
    await state.set_state(Person.city)

@router.message(Person.city)
async def city_handler(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')
    await message.answer(f'Я запомнил твои данные вот\nИмя - {name}\nВозраст-{age}\nГород-{city}')
    await state.clear()



@router.message(Command('info'))
async def info_handler(message: Message):
    await message.answer('Можешь ознакомиться с панелью')



@router.message(Command('random'))
async def random_handler(message: Message):
    await message.answer('Щас верну тебе рандомный факт')
    fact = await get_fact()
    await message.answer(f'Факт - {fact}')


@router.message(Command('gpt'))
async def random_handler(message: Message, state: FSMContext):
    await message.answer('Что интересует? ')
    await state.set_state(GPTDialog.message)

@router.message(GPTDialog.message)
async def gpt_reply(message: Message):
    reply = await dialog_gpt_func(message.text)
    await message.answer(reply, reply_markup=get_back_keyboard())

@router.message(Command('talk'))
async def talk_handler(message: Message):
    await message.answer('С кем хочешь поговорить? ',reply_markup=get_persons_keyboard())


@router.message(Command('quiz'))
async def talk_handler(message: Message):
    await message.answer('Выберите тему для квиза: ', reply_markup=topic_keyboard())


