from aiogram import types

from aiogram.types import CallbackQuery

from keyboards.inline import communication
from keyboards.inline.callback_datas import communication_callback
from loader import dp


@dp.message_handler(text="Связь с Менеджером")
async def price_list(message: types.Message):
    await message.answer("Какому менеджеру вы хотите обратится?", reply_markup=communication)


@dp.callback_query_handler(communication_callback.filter(name="nastya"))
async def call_leonid(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("<a href='t.me/anastya_opt'>@nastya_opt</a>")
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(communication_callback.filter(name="evgeniya"))
async def call_sergey(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("<a href='t.me/Evgeniya_opt'>@Evgenia_opt</a>")
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(communication_callback.filter(name="sergey"))
async def call_dimon(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("<a href='t.me/Sergey_opt'>@Sergei_opt</a>")
    await call.message.edit_reply_markup(reply_markup=None)
