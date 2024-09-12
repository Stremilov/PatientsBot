from datetime import datetime

from aiogram import types, F
from aiogram.filters import Command

from app.database import SessionLocal
from app.keyboards.reply.usermodes import main_kb
from app.loader import dp
from app.repositories.patient_repository import PatientRepository


@dp.message(Command("get_patients_count_by_day"))
@dp.message(F.text == "📋 Получить пациентов за эту неделю 📋")
async def get_patients_count_by_day(message: types.Message):
    session = SessionLocal()
    patient_repo = PatientRepository(session)
    counts = patient_repo.get_patients_count_by_day()

    days_of_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье",
    }
    response = "<b>Пациенты по дням</b>\n"

    patients_count_by_day = {day: 0 for day in days_of_week.values()}

    for date_obj, count in counts:
        day_name = days_of_week[date_obj.weekday()]
        patients_count_by_day[day_name] += count

    for day_name, count in patients_count_by_day.items():
        response += f"<b>{day_name}:</b> {count} пациентов\n"

    await message.answer(response, parse_mode="html", reply_markup=main_kb())