from aiogram import types

from loader import dp


@dp.message_handler(text="Условия работы!")
async def work_condition(message: types.Message):
    text = [
        "Условия работы",
        " Минимальный заказ от 5000 руб.",
        " Отправляем по всей РФ и в страны СНГ",
        " Отправка в течение 2 суток",
        " Чтобы сделать заказ, пришли из нашего прайс листа фото "
        "товара и количество менеджеру , он поможет оформить заказ!"
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(text="Яндекс Диск")
async def work_condition(message: types.Message):
    await message.answer("https://yadi.sk/d/f62qjG1PeDmpwA")


@dp.message_handler(text="Рестарт")
async def bot_start(message: types.Message):
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}! \n'
                         f'Я - GoodOptBOT, бот созданный чтобы помогать команде GoodOpt.')
