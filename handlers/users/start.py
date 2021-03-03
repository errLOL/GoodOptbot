from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}! \n'
                         f'Я - GoodOptBOT, бот созданный чтобы помогать команде GoodOpt.', reply_markup=menu)
