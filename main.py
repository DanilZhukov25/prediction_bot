import os
import random
import logging
from datetime import datetime
import asyncio
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()
telegram_token = os.getenv('ORACULUM_MYSTIC_BOT_TOKEN')
bot = Bot(token=telegram_token)
# CHAT_ID = os.getenv('TEST_CHAT_ID')
dp = Dispatcher()


async def get_bot_username(message: Message):
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    return bot_username


prediction_list = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется — «да»",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят — «да»",
    "Пока не ясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ — «нет»",
    "По моим данным — «нет»",
    "Перспективы не очень хорошие",
    "Весьма сомнительно"
]


@dp.message(lambda message: message.text and f"@Oraculum_MysticBot " in message.text)
async def reply_to_mention(message: Message):
    random_response = random.choice(prediction_list)
    await message.reply(random_response)


@dp.message(Command("prediction"))
async def prediction_for_the_message(message: Message):
    random_response = random.choice(prediction_list)
    await message.reply(random_response)


async def main():
    print("Бот запущен, время запуска: " + datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
