from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == 'feeling_bot')
async def feel_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Привет')


@router.callback_query(F.data == 'text_send')
async def text_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Напиши текст для рассылки')
