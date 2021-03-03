from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import communication_callback

communication = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Сергей",
            callback_data=communication_callback.new(name="sergey")
        ),
        InlineKeyboardButton(
            text="Анастасия",
            callback_data="manager:nastya"
        ),
        InlineKeyboardButton(
            text="Евгения",
            callback_data="manager:evgeniya"
        )
    ]
])
