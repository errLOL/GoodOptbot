from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Условия работы"),
            KeyboardButton(text="Прайс лист"),
            KeyboardButton(text="Яндекс Диск")
        ],
        [
            KeyboardButton(text="Связь с Менеджером"),
            KeyboardButton(text="Наши каналы"),
            KeyboardButton(text="Для жалоб и предложений")
        ],
        [
            KeyboardButton(text="Рестарт")
        ]
    ],
    resize_keyboard=True

)
