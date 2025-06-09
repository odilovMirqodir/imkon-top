import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import TOKEN
from routers.message_handler import message_router
from botcommand.botcommand import set_commands
from routers.call_back import call_back

TOKEN = TOKEN

dp = Dispatcher()
dp.include_router(message_router)
dp.include_router(call_back)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
