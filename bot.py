import sys
import asyncio
import logging
from config import TOKEN
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from handlers import test_handler, start_handler
from middleware.middleware import TimeRestrictionMiddleware
from middleware.user_db import UserDBMiddleware


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(test_handler.test_router, start_handler.start_router)
    dp.message.middleware(TimeRestrictionMiddleware())
    dp.callback_query.outer_middleware(UserDBMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
