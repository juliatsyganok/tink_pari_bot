from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
import asyncio
from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import  StateFilter
from users_states import UserStates

from keyboard_helper import get_keyboard, keyboards
import pari_serves as ps

import storage.user_repository as user_storage


storage = MemoryStorage()
Bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    user_storage.save_user(message.from_user.username, message.chat.id)
    kb = keyboards[UserStates.BASE]
    await message.answer('Привет! я пари-бот', reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(F.text == 'Мои пари', StateFilter(UserStates.BASE))
async def start(message: types.Message):
    text = 'Твои пари'
    paris = ps.get_paris(message.from_user.id)
    for pari in paris:
        text += '\n' + pari
    await message.answer(text)

@dp.message(F.text == 'Создать пари', StateFilter(UserStates.BASE))
async def start(message: types.Message, state: FSMContext):
    text = ps.set_pari_name()
    await message.answer(text)
    await state.set_state(UserStates.CREATE_PARI)

@dp.message(StateFilter(UserStates.CREATE_PARI))
async def set_pari_name(message: types.Message, state: FSMContext):
    text = ps.set_pari_taker()
    await message.answer(text)
    await state.set_state(UserStates.SETTING_PARI_TAKER)

@dp.message(StateFilter(UserStates.SETTING_PARI_TAKER))
async def set_pari_name(message: types.Message, state: FSMContext):
    text = ps.pari_created()
    await message.answer(text)
    await state.set_state(UserStates.BASE)

async def main():
    await dp.start_polling(Bot)

if __name__ == '__main__':
    asyncio.run(main())

