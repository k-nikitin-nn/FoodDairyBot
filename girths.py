import re
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import general


class Girth(StatesGroup):
    wait_date = State()
    wait_neck = State()
    wait_breast = State()
    wait_back = State()
    wait_belly = State()
    wait_thigh = State()
    wait_leg = State()
    wait_hand = State()
    wait_waist = State()
    wait_height = State()
    wait_weight = State()


girth_config = {
    "wait_date": {"state": Girth.wait_date},
    "wait_neck": {},
    "wait_breast": {},
    "wait_back": {},
    "wait_belly": {},
    "wait_thigh": {},
    "wait_leg": {},
    "wait_hand": {},
    "wait_waist": {},
    "wait_height": {},
    "wait_weight": {}
}


async def girth_start(message: types.Message):
    await message.answer("Укажите дату замеров в формате '01.01.0001':")
    await Girth.wait_date.set()


def register_profile_handlers(dp):
    @dp.message_handler(state=Girth.wait_date)
    async def girth_date_filled(message: types.Message, state: FSMContext):
        if general.is_date_incorrect(message.text):
            await message.answer("Дата замеров введена не корректно.")
            return

        await state.update_data(date=datetime.strptime(message.text, "%d.%m.%Y"))
        await Girth.next()

        await message.answer("Обхват шеи (см.):")

    @dp.message_handler(state=Girth.wait_neck)
    async def girth_neck_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват шеи введен не корректно.")
            return

        await state.update_data(neck=int(message.text))
        await Girth.next()

        await message.answer("Обхват груди (см.):")

    @dp.message_handler(state=Girth.wait_breast)
    async def girth_breast_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват груди введен не корректно.")
            return

        await state.update_data(breast=int(message.text))
        await Girth.next()

        await message.answer("Обхват спины (см.):")

    @dp.message_handler(state=Girth.wait_back)
    async def girth_back_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват спины введен не корректно.")
            return

        await state.update_data(back=int(message.text))
        await Girth.next()

        await message.answer("Обхват живота (см.):")

    @dp.message_handler(state=Girth.wait_belly)
    async def girth_belly_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват живота введен не корректно.")
            return

        await state.update_data(belly=int(message.text))
        await Girth.next()

        await message.answer("Обхват бедра (см.):")

    @dp.message_handler(state=Girth.wait_thigh)
    async def girth_thigh_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват бедра введен не корректно.")
            return

        await state.update_data(thigh=int(message.text))
        await Girth.next()

        await message.answer("Обхват голени (см.):")

    @dp.message_handler(state=Girth.wait_leg)
    async def girth_leg_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват голени введен не корректно.")
            return

        await state.update_data(leg=int(message.text))
        await Girth.next()

        await message.answer("Обхват руки (см.):")

    @dp.message_handler(state=Girth.wait_hand)
    async def girth_hand_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват руки введен не корректно.")
            return

        await state.update_data(hand=int(message.text))
        await Girth.next()

        await message.answer("Обхват талии (см.):")

    @dp.message_handler(state=Girth.wait_waist)
    async def girth_waist_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Обхват талии введен не корректно.")
            return

        await state.update_data(waist=int(message.text))
        await Girth.next()

        await message.answer("Рост (см.):")

    @dp.message_handler(state=Girth.wait_height)
    async def girth_height_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Рост введен не корректно.")
            return

        await state.update_data(height=int(message.text))
        await Girth.next()

        await message.answer("Вес (кг.):")

    @dp.message_handler(state=Girth.wait_weight)
    async def girth_height_filled(message: types.Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer("Вес введен не корректно.")
            return

        await state.update_data(weight=float(message.text))
        await Girth.next()

        await message.answer("Замеры тела сохранены.")




