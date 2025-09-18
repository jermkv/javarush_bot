from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Person

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message, state: FSMContext):
    await message.answer('Привет а как тебя зовут?')
    await state.set_state(Person.name)


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


