from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import price_callback

price = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="ШАПКИ КЕПКИ РЮКЗАКИ",
                                         callback_data=price_callback.new(item="hats_caps_backpacks")
                                     ),
                                     InlineKeyboardButton(
                                         text="НОВИНКИ",
                                         callback_data="price:new"
                                     )],
                                 [
                                     InlineKeyboardButton(
                                         text="НАУШНИКИ И КОЛОНКИ",
                                         callback_data="price:sound"
                                     ),
                                     InlineKeyboardButton(
                                         text="ЧАСЫ БРАСЛЕТЫ КОРОБКИ ДЛЯ ЧАСОВ",
                                         callback_data="price:watch_bracelets"
                                     )],
                                 [
                                     InlineKeyboardButton(
                                         text="ЭЛЕКТРОНКИ",
                                         callback_data="price:e-sigs"
                                     ),
                                     InlineKeyboardButton(
                                         text="ЭЛЕКТРОНИКА И АКССЕСУАРЫ",
                                         callback_data="price:electronics"
                                     )]

                             ])
