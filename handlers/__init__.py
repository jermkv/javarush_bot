from aiogram import  Router
from .commands_handler import router as start_router
from .text_handler import router as text_router
from .callbacks_handler import router as callbacks_router

router = Router()

router.include_routers(start_router, text_router, callbacks_router)
