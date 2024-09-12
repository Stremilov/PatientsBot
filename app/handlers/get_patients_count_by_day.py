from aiogram import types
from aiogram.filters import Command

from app.database import SessionLocal
from app.loader import dp
from app.repositories.patient_repository import PatientRepository


@dp.message(Command('get_patients_count_by_day'))
async def get_patients_count_by_day(message: types.Message):
    session = SessionLocal()
    patient_repo = PatientRepository(session)
    counts = patient_repo.get_patients_count_by_day()

    days_of_week = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
    response = "Пациенты по дням:\n"

    patients_count_by_day = {day: 0 for day in days_of_week.values()}

    for date, count in counts:
        day_name = days_of_week[date.weekday()]
        patients_count_by_day[day_name] += count

    for day_name, count in patients_count_by_day.items():
        response += f"{day_name}: {count} пациентов\n"

    await message.reply(response)
