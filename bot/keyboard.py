from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inl_b_1 = InlineKeyboardButton(text='Начать', callback_data='startg')
kb_inl = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(inl_b_1)

loc_req = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить геолокацию', request_location=True))

r_1 = InlineKeyboardButton(text='1 км', callback_data='1km')
r_2 = InlineKeyboardButton(text='2.5 км', callback_data='2.5km')
r_3 = InlineKeyboardButton(text='5 км', callback_data='5km')
r_4 = InlineKeyboardButton(text='10 км', callback_data='10km')
kb_r = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(r_1, r_2, r_3, r_4)
