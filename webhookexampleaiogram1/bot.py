import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

from config import *
from databases import Database

database = Database(DATABASE_URL)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    await database.connect()
    await database.execute(
        """CREATE TABLE messages (
            id SERIAL PRIMARY KEY,
            telegram_id INTEGER NOT NULL,
            text text NOT NULL
            );"""
    )


async def on_shutdown(dispatcher):
    await bot.delete_webhook()
    await database.disconnect()


async def save(user_id, text):
    await database.execute(
        f"INSERT INTO messages(telegram_id, text) " f"VALUES (:telegram_id, :text)",
        values={"telegram_id": user_id, "text": text},
    )


async def read(user_id):
    results = await database.fetch_all('SELECT text '
                                       'FROM messages '
                                       'WHERE telegram_id = :telegram_id ',
                                       values={'telegram_id': user_id})
    return [next(result.values()) for result in results]


@dp.message_handler()
async def echo(message: types.Message):
    await save(message.from_user.id, message.text)
    messages = await read(message.from_user.id)
    await message.answer(messages)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
