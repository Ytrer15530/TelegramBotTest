import logging
from aiogram import types, F, Router
import pyjokes
import random
import requests
from utils import get_fruits
from keyboard import keyboard
# from handlers.weather_handler import weather_router, weather_message_handler

test_router = Router()


# @test_router.message(F.text == "Tell a joke")
# async def joke(message: types.Message):
#     logging.info(f'{message.from_user} Tell a joke')
#     joke = pyjokes.get_joke()
#     await message.answer(joke)
#
#
# @test_router.message(F.text == "Get Fruits")
# async def get_category(message: types.Message):
#     logging.info(f"{message.from_user.first_name} FRUITS")
#     await message.answer('Wait...')
#     for item in get_fruits():
#         card = \
#             f"id - {item['id']}\n" \
#             f"fruit - {item['name']}\n" \
#             f"Family - {item['family']}\n" \
#
#         await message.answer(card)
#
#
# @test_router.message(F.text == "Coffee")
# async def coffee(message: types.Message):
#     logging.info(f"{message.from_user.first_name} COFFEE")
#     api = 'https://coffee.alexflipnote.dev/random.json'
#     await message.answer("Wait...")
#     response = requests.get(api).json()
#     # img = types.URLInputFile(response['file'])
#     card = f"Coffee: {response['file']}"
#     await message.answer(card)
#
#
# @test_router.message(F.text == "Weather")
# async def change_keyboard_to_weather(message: types.Message):
#     logging.info(f"{message.from_user.first_name} WEATHER")
#     await message.answer("Choose city", reply_markup=keyboard_weather)
#     weather_router.register_message_handler(weather_message_handler)
