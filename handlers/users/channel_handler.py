from aiogram import types

from aiogram.types import CallbackQuery

from keyboards.inline import channel
from keyboards.inline.callback_datas import channel_callback
from loader import dp


@dp.message_handler(text="Наши каналы")
async def price_list(message: types.Message):
    await message.answer("Какой именно канал тебе нужен?", reply_markup=channel)


@dp.callback_query_handler(channel_callback.filter(name="electronic"))
async def call_electronic(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/aks_opt")
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(channel_callback.filter(name="clothes"))
async def call_clothes(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("https://t.me/goodoptmsk")
    await call.message.edit_reply_markup(reply_markup=None)

