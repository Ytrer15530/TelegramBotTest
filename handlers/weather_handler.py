import logging
from aiogram import types, F, Router
import requests
from keyboard import keyboard, buttons

weather_router = Router()


@weather_router.message()
async def weather_message_handler(message: types.Message):
    logging.info(f'{message.from_user.first_name} {message.text}')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q={message.text}&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in {message.text} is {temperature}°C
    {condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])
