from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# kb = [
#     [
#         types.KeyboardButton(text="Weather"),
#         types.KeyboardButton(text="Tell a Joke"),
#         types.KeyboardButton(text="Coffee"),
#         types.KeyboardButton(text="Get Fruits"),
#         types.KeyboardButton(text="random int"),
#     ],
# ]
#
#
# keyboard = types.ReplyKeyboardMarkup(
#     keyboard=kb,
#     resize_keyboard=True,
#     input_field_placeholder="choose menu"
# )

buttons = ['Warsaw', 'Kyiv', 'Tokyo', 'Shanghai', 'London']

keyboard_buttons = []
for button in buttons:
    keyboard_buttons.append([KeyboardButton(text=button)])

keyboard = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True, selective=True)
