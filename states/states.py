from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    ism_familya = State()
    phone_number = State()
    passport_id = State()
    passport_image = State()
    confirmation = State()


class CheckForm(StatesGroup):
    image = State()
