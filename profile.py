from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import db
import general


class ProfileUser(StatesGroup):
    wait_username = State()
    wait_lastname = State()
    wait_birthday = State()
    wait_email = State()


async def profile_start(message: types.Message):
    await message.answer("Привет! Давай знакомиться!")
    await message.answer("Как тебя зовут?")
    await ProfileUser.wait_username.set()


profile_config = {
    "wait_username": {
        "state": ProfileUser.wait_username
    },
    "wait_lastname": {"state": ProfileUser.wait_lastname},
    "wait_birthday": {"state": ProfileUser.wait_birthday},
    "wait_email": {"state": ProfileUser.wait_email}
}


def register_profile_handlers(dp):
    @dp.message_handler(state=ProfileUser.wait_username)
    async def profile_username_filled(message: types.Message, state: FSMContext):
        await update_data(message, state, ProfileUser, {"name": message.text})

    @dp.message_handler(state=ProfileUser.wait_lastname)
    async def profile_lastname_filled(message: types.Message, state: FSMContext):
        await state.update_data(last_name=message.text)
        await ProfileUser.next()

        await message.answer("Введи дату рождения в формате '01.01.0001'")

    @dp.message_handler(state=ProfileUser.wait_birthday)
    async def profile_birthday_filled(message: types.Message, state: FSMContext):
        if general.is_email_incorrect(message.text):
            await message.answer("Дата рождения введена не корректно.")
            return

        await state.update_data(birthday=datetime.strptime(message.text, "%d.%m.%Y"))
        await ProfileUser.next()

        await message.answer("Введи email.")

    @dp.message_handler(state=ProfileUser.wait_email)
    async def profile_email_filled(message: types.Message, state: FSMContext):
        if general.is_date_incorrect(message.text):
            await message.answer("Email введен не корректно.")
            return

        await state.update_data(email=message.text)

        data = await state.get_data()
        db.create_user(data)

        await message.answer("Спасибо.")


def check_f(fn):
    async def wrapped(message, state, description_states, data):
        await fn(message, state, description_states, data)
        await message.answer("Введи свою фамилию.")

    return wrapped


@check_f
async def update_data(message, state, description_states, data):
    await state.update_data(data)
    await description_states.next()
