from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


feedback = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Менеджер Егор",
            callback_data='garat'
        )
    ]
])
