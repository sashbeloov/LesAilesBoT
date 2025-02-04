
import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo, message
import asyncio
from random import randint

from pyexpat.errors import messages

from funtions import *

from russian import handle_text_r

TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"



from lesailesbot import *


# file_path_bb = "images/doublechickenchiz.jpg"
# caption_text_bb = (
#         f"Nomi: {name}"
#         f"Narxi: {price}so'm"
#     )

# burgerlarrr = {
#     'Klassik': {
#         'narx': 15000,
#         'rasm': "images/classic.jpg"
#     },
#     "1+1 Barbekyu burger": {
#         'narx': 18000,
#         'rasm': "images/1+1barbekyu.jpg"
#     },
#     '1+1 Sezar burger': {
#         'narx': 20000,
#         'rasm': "images/1+1Sezarburger.jpg"
#     },
#     "Singer": {
#         'narx': 22000,
#         'rasm': "images/singer.jpg"
#     },
#     "Chiken chiz": {
#         'narx': 25000,
#         'rasm': "images/chickenchiz.jpg"
#     },
#     "Xalapenyo burger": {
#         'narx': 27000,
#         'rasm': "images/xalapenyo.jpg"
#     },
#     "Biger": {
#         'narx': 30000,
#         'rasm': "images/bigger.jpg"
#     },
#     "Dabl chiken chiz": {
#         'narx': 32000,
#         'rasm': "images/doublechickenchiz.jpg"
#     }
# }
#
#
# async def burgerlarr(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]["holat"] = "burgerlar"
#     item = message.text
#
#     # Agar mahsulot lug'atda bo'lsa
#     if item in tovuq_dict:
#         info = burgerlarrr[item]
#         narx = info['narx']
#         rasm_manzi = info['rasm']
#
#         # Klaviatura tugmalari
#         asosiy_tugmalar = [
#             [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
#         ]
#         reply_keyboard = types.ReplyKeyboardMarkup(keyboard=asosiy_tugmalar, resize_keyboard=True)
#
#         inline_tugmalar = [
#             [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
#              types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
#              types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}")],
#             [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}")],
#         ]
#         inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_tugmalar, resize_keyboard=True)
#
#         # Caption yaratamiz (oddiy qilib)
#         caption_text = f"Nomi: {item}\nNarxi: {narx} so'm"
#
#         await message.answer("Miqdorni belgilang", reply_markup=reply_keyboard)
#         await message.reply_photo(
#             caption=caption_text,
#             photo=types.FSInputFile(path=rasm_manzi),
#             parse_mode="Markdown",
#             reply_markup=inline_keyboard
#         )
#     else:
#         await message.answer("Bunday mahsulot topilmadi!")
#
