import re
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import db
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


def girths_structure():
    return {
        "neck": {"name_ru": "Шея", "unit": "см", "dates": {}},
        "breast": {"name_ru": "Грудь", "unit": "см", "dates": {}},
        "back": {"name_ru": "Спина", "unit": "см", "dates": {}},
        "waist": {"name_ru": "Талия", "unit": "см", "dates": {}},
        "belly": {"name_ru": "Живот", "unit": "см", "dates": {}},
        "thigh": {"name_ru": "Бедра", "unit": "см", "dates": {}},
        "hand": {"name_ru": "Правая рука", "unit": "см", "dates": {}},
        "leg": {"name_ru": "Правая нога", "unit": "см", "dates": {}},
        "weight": {"name_ru": "Вес", "unit": "кг", "dates": {}}
    }


async def show_girths(message: types.Message):
    result = db.get_girths(message.from_user.id)
    if not result:
        await message.answer("Измерения еще не введены.")

    await message.answer("Динамика измерений \n\n")

    girths = girths_structure()

    for elem in result:
        for key, value in girths.items():
            value.get("dates")[datetime.strftime(elem.date, '%d.%m.%Y')] = vars(elem)[key]

    for key, value in girths.items():
        mes = value.get("name_ru") + "\n\n"
        unit = value.get("unit")

        for date, girth in value.get("dates").items():
            mes = mes + f"{date} - {girth} {unit}. \n"

        await message.answer(mes)


async def girth_start(message: types.Message):
    await message.answer("Укажите дату замеров в формате '01.01.0001':")
    await Girth.wait_date.set()


def register_girth_handlers(dp):
    @dp.message_handler(state=Girth.wait_date)
    async def girth_date_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="date",
            extra=general.string_to_date,
            next_message="Обхват шеи (см.):",
            error="Дата замеров введена не корректно.",
            check=general.is_date_incorrect
        )

    @dp.message_handler(state=Girth.wait_neck)
    async def girth_neck_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="neck",
            extra=general.string_to_int,
            next_message="Обхват груди (см.):",
            error="Обхват шеи введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_breast)
    async def girth_breast_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="breast",
            extra=general.string_to_int,
            next_message="Обхват спины (см.):",
            error="Обхват груди введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_back)
    async def girth_back_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="back",
            extra=general.string_to_int,
            next_message="Обхват живота (см.):",
            error="Обхват спины введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_belly)
    async def girth_belly_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="belly",
            extra=general.string_to_int,
            next_message="Обхват бедра (см.):",
            error="Обхват живота введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_thigh)
    async def girth_thigh_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="thigh",
            extra=general.string_to_int,
            next_message="Обхват голени (см.):",
            error="Обхват бедра введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_leg)
    async def girth_leg_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="leg",
            extra=general.string_to_int,
            next_message="Обхват руки (см.):",
            error="Обхват голени введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_hand)
    async def girth_hand_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="hand",
            extra=general.string_to_int,
            next_message="Обхват талии (см.):",
            error="Обхват руки введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_waist)
    async def girth_waist_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="waist",
            extra=general.string_to_int,
            next_message="Рост (см.):",
            error="Обхват талии введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_height)
    async def girth_height_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="height",
            extra=general.string_to_int,
            next_message="Вес (кг.):",
            error="Рост введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_weight)
    async def girth_height_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="weight",
            extra=general.string_to_int,
            next_message="Замеры тела сохранены.",
            error="Вес введен не корректно.",
            check=general.is_not_number
        )

        data = await state.get_data()
        db.create_girth(data)
