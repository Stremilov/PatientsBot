import re
from datetime import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.loader import dp
from app.repositories.patient_repository import PatientRepository
from app.states.usermodes import AddPatientForm


def validate_string(input_string):
    pattern = r'^[а-яА-Я0-9]+$'

    if re.match(pattern, input_string):
        return True
    else:
        return False


def check_age(date_of_birth):
    try:
        birth_date = datetime.strptime(date_of_birth, "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        return 0 < age < 100
    except ValueError:
        return False


@dp.message(Command("add_patient"))
async def add_patient(message: types.Message, state: FSMContext):
    await state.set_state(AddPatientForm.registerUserInfo)
    await message.answer("Введите ФИО пациента:")


@dp.message(AddPatientForm.registerUserInfo)
async def get_user_info(message: types.Message, state: FSMContext):
    user_data = message.text

    if all(validate_string(word) for word in user_data.split()):
        await message.answer("Введите дату рождения в формате xx.xx.xxxx")
        await state.update_data(user_data=user_data)
        await state.set_state(AddPatientForm.registerUserAge)
    else:
        await message.answer(
            "Неправильный формат ввода данных\n"
            "Входные данные не должны содержать специальных символов"
        )


@dp.message(AddPatientForm.registerUserAge)
async def get_date_of_birth_and_register_user(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_age = message.text
    user_info = user_data.get("user_data")

    db = SessionLocal()

    patient_repo = PatientRepository(db)

    if check_age(user_age):
        patient_repo.add_patient(name=user_info, date_of_birth=user_age)
        await message.answer("Пациент успешно помещён в базу")
        await state.set_state(None)
    else:
        await message.answer("Некорректный возраст или формат входных данных")
