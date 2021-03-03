from aiogram import Dispatcher

from filters.privat_chat import IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
