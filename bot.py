import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("✅ Бот живой! Я тебя вижу.\n\nНапиши любое слово — я должен ответить.")

@dp.message()
async def any_message(message: Message):
    await message.answer(f"✅ Я получил твое сообщение:\n{message.text}")

async def main():
    print("🤖 Тестовый бот запущен!")
    await dp.start_polling(bot, drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
