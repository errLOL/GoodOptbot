from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('Вы начали тестирование \n'
                         'Вопрос номер 1 \n\n'
                         'Вы часто занмаетесь бесмысленными делами?')

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Вопрос номер 2 \n\n"
                         "Ваша память ухудшилось и вы помните то, что было давно, но забываете"
                         "недавние события?")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text
    await message.answer(f"Ответ №1: {answer1} \n"
                         f"Ответ №2: {answer2}")
    await state.finish()
