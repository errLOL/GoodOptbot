from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import channel_callback

channel = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Одежда",
            callback_data="channel:clothes"
        ),
        InlineKeyboardButton(
            text="Электроника",
            callback_data=channel_callback.new(name="electronic")
        )
    ]
])
