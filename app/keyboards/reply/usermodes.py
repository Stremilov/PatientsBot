from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_kb():
    builder = ReplyKeyboardBuilder()

    builder.add(types.KeyboardButton(text="👤 Добавить пациента 👤"))
    builder.add(types.KeyboardButton(text="👥 Получить пациентов за сегодня 👥"))
    builder.add(types.KeyboardButton(text="📋 Получить пациентов за эту неделю 📋"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
