import logging
from aiogram import types, F, Router
import pyjokes
import random
import requests
from utils import get_fruits, resp

test_router = Router()


# @test_router.message(F.text == "Tell a joke")
# async def joke(message: types.Message):
#     logging.info(f'{message.from_user} Tell a joke')
#     joke = pyjokes.get_joke()
#     await message.answer(joke)
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

@test_router.message(F.text == "Kyiv")
async def kyiv_weather(message: types.Message):
    logging.info(f'{message.from_user.first_name} Kyiv')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q=kyiv&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in Kyiv is {temperature}°C
{condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])

@test_router.message(F.text == "London")
async def london_weather(message: types.Message):
    logging.info(f'{message.from_user.first_name} London')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q=london&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in London is {temperature}°C
{condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])


@test_router.message(F.text == "Tokyo")
async def tokio_weather(message: types.Message):
    logging.info(f'{message.from_user.first_name} Tokyo')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q=tokyo&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in Tokyo is {temperature}°C
{condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])


@test_router.message(F.text == "Warsaw")
async def warsaw_weather(message: types.Message):
    logging.info(f'{message.from_user.first_name} Warsaw')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q=warsaw&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in Warsaw is {temperature}°C
{condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])


@test_router.message(F.text == "Shanghai")
async def shanghai_weather(message: types.Message):
    logging.info(f'{message.from_user.first_name} Shanghai')
    api = f'https://api.weatherapi.com/v1/current.json?key=2a09ee3bbc5e4b96b82133730241301&q=shanghai&aqi=no'
    await message.answer("wait...")
    resp = requests.get(api).json()
    temperature = resp['current']['temp_c']
    condition = resp['current']['condition']['text']
    icon = resp['current']['condition']['icon']
    card = f'''Weather in Shanghai is {temperature}°C
{condition}'''
    await message.answer(card)
    await message.answer_photo(icon[2:])
