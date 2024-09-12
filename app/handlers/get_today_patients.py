from aiogram import types
from aiogram.filters import Command

from app.database import SessionLocal
from app.loader import dp
from app.repositories.patient_repository import PatientRepository


@dp.message(Command('get_today_patients'))
async def get_today_patients(message: types.Message):
    session = SessionLocal()
    patient_repo = PatientRepository(session)
    patients = patient_repo.get_today_patients()

    if patients:
        response = "Сегодняшние пациенты:\n"
        for patient in patients:
            response += f"{patient.name}, Дата рождения: {patient.date_of_birth}\n"
    else:
        response = "Сегодня не было пациентов."

    await message.answer(response)
