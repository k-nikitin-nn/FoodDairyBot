# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils.callback_data import CallbackData
#
# from bot import dp
#
#
# class Entry(StatesGroup):
#     ...


# cb = CallbackData("post", "id", "action")


# def get_keyboard():
# buttons = [
#     types.InlineKeyboardButton(text="Завтрак", callback_data=cb.new(action="decr")),
#     types.InlineKeyboardButton(text="Обед", callback_data=cb.new(action="incr")),
#     types.InlineKeyboardButton(text="Ужин", callback_data=cb.new(action="finish")),
#     types.InlineKeyboardButton(text="Вода", callback_data=cb.new(action="finish")),
#     types.InlineKeyboardButton(text="Перекус", callback_data=cb.new(action="finish"))
# ]
# keyboard = types.InlineKeyboardMarkup(row_width=2)
# keyboard.add(*buttons)
# return keyboard

# async def entries_start(message: types.Message):
# button = types.InlineKeyboardButton(
#     text="Лайкнуть",
#     callback_data=cb.new(id=5, action="like")
# )


# @dp.callback_query_handler(cb.filter())
# async def callbacks(call: types.CallbackQuery, callback_data: dict):
#     post_id = callback_data["id"]
#     action = callback_data["action"]
#
#
# def register_entries_handlers(dp):
#     ...
