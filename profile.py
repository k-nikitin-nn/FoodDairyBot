from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import db
import general
from config import menu


class ProfileUser(StatesGroup):
    wait_username = State()
    wait_lastname = State()
    wait_birthday = State()
    wait_email = State()


async def profile_start(message: types.Message):
    await message.answer("Привет! Давай знакомиться!")
    await message.answer("Как тебя зовут?")
    await ProfileUser.wait_username.set()


def register_profile_handlers(dp):
    @dp.message_handler(state=ProfileUser.wait_username)
    async def profile_username_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=ProfileUser,
            data="name",
            next_message="Введи свою фамилию:")

    @dp.message_handler(state=ProfileUser.wait_lastname)
    async def profile_lastname_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=ProfileUser,
            data="last_name",
            next_message="Введи дату рождения в формате '01.01.0001'")

    @dp.message_handler(state=ProfileUser.wait_birthday)
    async def profile_birthday_filled(message: types.Message, state: FSMContext):
        await general.update_data(
            message=message,
            state=state,
            states=ProfileUser,
            data="birthday",
            extra=general.string_to_date,
            next_message="Введи email:",
            error="Дата рождения введена не корректно.",
            check=general.is_date_incorrect
        )

    @dp.message_handler(state=ProfileUser.wait_email)
    async def profile_email_filled(message: types.Message, state: FSMContext):
        res = await general.update_data(
            message=message,
            state=state,
            states=ProfileUser,
            data="email",
            next_message="Спасибо. Данные сохранены",
            error="Email введен не корректно.",
            check=general.is_email_incorrect
        )

        if res is None:
            await message.answer(menu)

            data = await state.get_data()
            db.create_user(data)
