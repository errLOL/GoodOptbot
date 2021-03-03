from aiogram import types

from aiogram.types import CallbackQuery

from keyboards.inline import feedback
from loader import dp


@dp.message_handler(text="Для жалоб и предложений")
async def price_list(message: types.Message):
    await message.answer("Вот кому ты можешь обратится", reply_markup=feedback)


@dp.callback_query_handler(text="garat")
async def call_electronic(call: CallbackQuery):
    await call.message.answer("вот твой запрос")
    await call.message.answer("<a href='t.me/Good_opt_Egor'>@goodopt_egor</a>")
    await call.message.edit_reply_markup(reply_markup=None)


