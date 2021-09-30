import re
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Measure(StatesGroup):
    wait_date = State()
    wait_neck_size = State()
    wait_breast_size = State()
    wait_back_size = State()
    wait_stomach_size = State()
    wait_thigh_size = State()
    wait_leg_size = State()
    wait_hand_size = State()
    wait_waist_size = State()
    wait_height = State()
    wait_weight = State()


async def measure_start(message: types.Message):
    await message.answer("Укажите дату замеров в формате '01.01.0001':")
    await Measure.wait_date.set()


def register_profile_handlers(dp):
    @dp.message_handler(state=Measure.wait_date)
    async def measure_date_filled(message: types.Message, state: FSMContext):
        pattern = r"(?:0[1-9]|[12]\d|3[01])([.])(?:0[1-9]|1[012])\1(?:19|20)\d\d$"
        if re.match(pattern, message.text.strip()) is None:
            await message.answer("""Дата замеров введена не корректно. Пожалуйста, введи дату замеров ещё раз.""")
            return

        await state.update_data(date=datetime.strptime(message.text.strip(), "%d.%m.%Y"))
        await Measure.next()

        await message.answer("Размер шеи (см.):")

