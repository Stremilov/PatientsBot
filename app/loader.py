from aiogram import Dispatcher, Bot, Router
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

form_router = Router()
dp.include_router(form_router)
