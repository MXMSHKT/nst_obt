from aiogram import Dispatcher, types
from bot_init import dp
from menu.markups import startup_markup
from menu.phrases import about_nst_msg, welcome_msg, help_msg


async def send_welcome(message: types.Message):
    await message.answer(
        text=welcome_msg,
        reply_markup=startup_markup,
        parse_mode='Markdown'
    )

async def send_help(message: types.Message):
    await message.answer(
        text=help_msg,
        reply_markup=startup_markup,
        parse_mode='Markdown'
    )

async def about_nst(message: types.Message):
    await message.answer(
        text=about_nst_msg,
        reply_markup=startup_markup,
        parse_mode='Markdown'
    )

def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_help, commands=['help'])
    dp.register_message_handler(about_nst, commands=['about'])

