import asyncio
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from handlers import router
import logging


#FSM - Машина состояний

async def main():
    logging.basicConfig(level=logging.INFO) #Логирование
    bot = Bot(TOKEN)  # Связывались с серверами тг с нашим токеном
    dp = Dispatcher()  # Ловит апдейты
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())

