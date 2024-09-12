from aiogram import types
from aiogram.filters import Command

from app.keyboards.reply.usermodes import main_kb
from app.loader import dp


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет, доктор! Я помогу вам вести учет пациентов.", reply_markup=main_kb())
