from aiogram import types

from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import price_callback
from keyboards.inline import price
from loader import dp


@dp.message_handler(text="Прайс лист")
async def price_list(message: types.Message):
    await message.answer("Какой прайс нужен ?", reply_markup=price)


@dp.callback_query_handler(price_callback.filter(item="hats_caps_backpacks"))
async def show_hats_caps_backpacks(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1510")


@dp.callback_query_handler(price_callback.filter(item="new"))
async def show_new(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1511")


@dp.callback_query_handler(price_callback.filter(item="sound"))
async def show_sound(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1512")


@dp.callback_query_handler(price_callback.filter(item="watch_bracelets"))
async def show_watch_bracelets(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1513")


@dp.callback_query_handler(price_callback.filter(item="e-sigs"))
async def show_esigs(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1514")


@dp.callback_query_handler(price_callback.filter(item="electronics"))
async def show_electronics(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk/1515")
