from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import  StateFilter
from users_states import UserStates


storage = MemoryStorage()
Bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Привет! я пари-бот')
    await state.set_state(UserStates.BASE)

@dp.message(Command('test'), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    await message.answer('Ты в состоянии BASE')

async def main():
    await dp.start_polling(Bot)

if __name__ == '__main__':
    asyncio.run(main())

