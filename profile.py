import re
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import db


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
        await state.update_data(name=message.text)
        await ProfileUser.next()

        await message.answer("Введи свою фамилию.")

    @dp.message_handler(state=ProfileUser.wait_lastname)
    async def profile_lastname_filled(message: types.Message, state: FSMContext):
        await state.update_data(last_name=message.text)
        await ProfileUser.next()

        await message.answer("Введи дату рождения в формате '01.01.0001'")

    @dp.message_handler(state=ProfileUser.wait_birthday)
    async def profile_birthday_filled(message: types.Message, state: FSMContext):
        pattern = r"(?:0[1-9]|[12]\d|3[01])([.])(?:0[1-9]|1[012])\1(?:19|20)\d\d$"
        if re.match(pattern, message.text.strip()) is None:
            await message.answer("""Дата рождения введена не корректно. Пожалуйста, введи дату рождения ещё раз.""")
            return

        await state.update_data(birthday=datetime.strptime(message.text.strip(), "%d.%m.%Y"))
        await ProfileUser.next()

        await message.answer("Введи email.")

    @dp.message_handler(state=ProfileUser.wait_email)
    async def profile_email_filled(message: types.Message, state: FSMContext):
        pattern = r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
        if re.match(pattern, message.text) is None:
            await message.answer("Email введен не корректно. Пожалуйста, введи email ещё раз.")
            return

        await state.update_data(email=message.text)

        data = await state.get_data()
        db.insert_db(data)

        await message.answer("Спасибо.")
