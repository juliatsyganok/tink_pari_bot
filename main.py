from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
import asyncio

Bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет! я эхо-бот')

@dp.message()
async def echo(message: types.Message):
   await message.answer(message.text)

async def main():
    await dp.start_polling(Bot, a=['0'])

if __name__ == '__main__':
    asyncio.run(main())

