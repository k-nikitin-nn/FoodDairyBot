# #!venv/bin/python
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from config import TOKEN
from profile import profile_start, register_profile_handlers

from models.database import DB_NAME
import db

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
        await message.answer(
            "Бот помогает \n\n"
            "Добавить замеры тела: /add_girths \n"
            "Добавить запись дневника: /add_entries \n"
            "Динамика замеров тела: /get_girths \n"
            "Список записей дневника: /get_entries \n")

register_profile_handlers(dp)

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


