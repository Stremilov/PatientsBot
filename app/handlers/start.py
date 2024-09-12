from aiogram import types
from aiogram.filters import Command

from app.loader import dp


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Привет, доктор! Я помогу вам вести учет пациентов.")