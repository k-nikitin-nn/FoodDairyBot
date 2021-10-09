from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import db
import general
from config import menu


class Girth(StatesGroup):
    wait_date = State()
    wait_neck = State()
    wait_breast = State()
    wait_back = State()
    wait_waist = State()
    wait_belly = State()
    wait_thigh = State()
    wait_hand = State()
    wait_foot = State()
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
        "foot": {"name_ru": "Правая нога", "unit": "см", "dates": {}},
        "weight": {"name_ru": "Вес", "unit": "кг", "dates": {}}
    }


async def show_girths(message: types.Message):
    result = db.get_girths(message.from_user.id)
    if not result:
        await message.answer("Замеры тела еще не введены.")
        await message.answer(menu)
        return

    await message.answer("Динамика измерений \n\n")

    girths = girths_structure()

    for elem in result:
        for key, value in girths.items():
            value.get("dates")[datetime.strftime(elem.date, '%d.%m.%Y')] = vars(elem)[key]

    for key, value in girths.items():
        mes = value.get("name_ru") + "\n\n"
        unit = value.get("unit")

        for date, girth in value.get("dates").items():
            mes = mes + f"{date} - {girth}.0 {unit}. \n"

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
            next_message="Обхват талии (см.):",
            error="Обхват спины введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_waist)
    async def girth_belly_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="waist",
            extra=general.string_to_int,
            next_message="Обхват живота (см.):",
            error="Обхват талии введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_belly)
    async def girth_thigh_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="belly",
            extra=general.string_to_int,
            next_message="Обхват бедер (см.):",
            error="Обхват живота введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_thigh)
    async def girth_foot_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="thigh",
            extra=general.string_to_int,
            next_message="Обхват правой руки (см.):",
            error="Обхват бедер введен не корректно.",
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
            next_message="Обхват правой ноги (см.):",
            error="Обхват правой руки введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_foot)
    async def girth_waist_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="foot",
            extra=general.string_to_int,
            next_message="Вес (кг.):",
            error="Обхват правой ноги введен не корректно.",
            check=general.is_not_number
        )

    @dp.message_handler(state=Girth.wait_weight)
    async def girth_height_filled(message: types.Message, state: FSMContext):
        res = await general.update_data(
            message=message,
            state=state,
            states=Girth,
            data="weight",
            extra=general.string_to_int,
            next_message="Спасибо. Замеры тела сохранены.",
            error="Вес введен не корректно.",
            check=general.is_not_number
        )

        if res is None:
            await message.answer(menu)

            data = await state.get_data()
            db.create_girth(data)
