from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Entry(StatesGroup):
    ...


async def entries_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["С пюрешкой", "Без пюрешки"]
    keyboard.add(*buttons)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
    # await Entry.wait_date.set()


def register_entries_handlers(dp):
    ...
