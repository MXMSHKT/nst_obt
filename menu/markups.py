from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Buttons
help_btn = KeyboardButton('/help')
about_btn = KeyboardButton('/about')
run_btn = KeyboardButton('/run')
confirm_btn = KeyboardButton('/confirm')
cancel_btn = KeyboardButton('/cancel')

# Markups
startup_markup = ReplyKeyboardMarkup(resize_keyboard=True)
startup_markup.add(run_btn).add(about_btn).add(help_btn)

confirm_markup = ReplyKeyboardMarkup(resize_keyboard=True)
confirm_markup.add(confirm_btn).add(cancel_btn)

cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_markup.add(cancel_btn)
