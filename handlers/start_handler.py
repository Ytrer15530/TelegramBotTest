from aiogram.filters import CommandStart
from aiogram import types, F, Router
import logging
from aiogram.utils.markdown import hbold
from keyboard import keyboard

start_router = Router()


# @start_router.message(CommandStart)
# async def command_start(message: types.Message):
#     logging.info(message.from_user)
#     await message.answer(f"Hi this is my first telegram bot. I'm watching you {hbold(message.from_user.first_name)}",
#                          reply_markup=keyboard)