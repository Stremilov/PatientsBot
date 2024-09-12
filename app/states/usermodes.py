from aiogram.fsm.state import State, StatesGroup


class AddPatientForm(StatesGroup):
    registerUserInfo = State()
    registerUserAge = State()
