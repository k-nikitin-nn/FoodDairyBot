# #!venv/bin/python
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from config import TOKEN
from profile import profile_start, register_profile_handlers
from girths import girth_start, register_girth_handlers, show_girths
# from entries import entries_start, register_entries_handlers

from models.database import DB_NAME
import db
from config import menu

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    """Обработка команды start. Вывод текста и меню
    Поиск пользователя в базе. Если не найден - предложить заполнить анкету.
    Если найден - показываем меню"""
    await state.finish()

    await message.answer("Добро пожаловать!")
    result = db.get_user(message.from_user.id)
    if not bool(result):
        await state.update_data(telegram_id=message.from_user.id)
        await profile_start(message)
    else:
        await message.answer(menu)


@dp.message_handler(commands=['add_girths'], state="*")
async def start_girths(message: types.Message, state: FSMContext):
    await state.finish()

    result = db.get_user(message.from_user.id)
    if bool(result):
        await state.update_data(user_id=result[0].id)
        await girth_start(message)
    else:
        await message.answer("Что-то пошло не так.")


@dp.message_handler(commands=['add_entries'], state="*")
async def start_girths(message: types.Message, state: FSMContext):
    await state.finish()

    result = db.get_user(message.from_user.id)
    if bool(result):
        await state.update_data(user_id=result[0].id)
        await entries_start(message)
    else:
        await message.answer("Что-то пошло не так.")


@dp.message_handler(commands=['get_girths'])
async def start_girths(message: types.Message):
    await show_girths(message)
    await message.answer(menu)


register_profile_handlers(dp)
# register_entries_handlers(dp)
register_girth_handlers(dp)

# @dp.message_handler(commands=['help'])
# async def help_handler(message: types.Message):
#     '''Обработка команды help. Вывод текста и меню'''

#     await message.answer(f'Привет, {message.from_user.first_name}!') 


# @dp.message_handler(lambda c: c.data == 'main_window')
# async def show_main_window(calback_query: types.CallbackQuery):
#     '''Главный экран'''


# @dp.message_handler()
# async def unknown_message(message: types.Message):
#     """Ответ на любое неожидаемое сообщение"""

@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")

if __name__ == '__main__':
    if not os.path.exists(DB_NAME):
        db.create()

    executor.start_polling(dp, skip_updates=True)


