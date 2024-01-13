from aiogram import types

kb = [
    [
        types.KeyboardButton(text="Warsaw"),
        types.KeyboardButton(text="Kyiv"),
        types.KeyboardButton(text="Tokyo"),
        types.KeyboardButton(text="Shanghai"),
        types.KeyboardButton(text="London"),
    ],
]


keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="choose menu"
)