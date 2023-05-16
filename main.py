import random
import json
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from telebot_settings import telebot_api_key
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=telebot_api_key)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

km1g_sh = 111.134861111  # км в 1 градусе широты
km1g_dolg = 111.321377778  # км в 1 градусе долготы
_1_10g_sh = km1g_sh / 10  # км в 0.1 градусе широты
_1_10g_dolg = km1g_dolg / 10  # км в 0.1 градусе долготы
_1_100g_sh = km1g_sh / 111.134861  # км в 0.00899807667 градусе широты близко к 1км
_1_100g_dolg = km1g_dolg / 111.3213777  # км в 0.00898300057 градусе долготы близко к 1км
sh_g_1km = 0.00899807667  # градусов широты в около 1км
dolg_g_1km = 0.00899807667  # градусов долготы в около 1км



inl_b_1 = InlineKeyboardButton(text='Начать', callback_data='startg')
kb_inl = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(inl_b_1)

loc_req = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить геолокацию', request_location=True))

r_1 = InlineKeyboardButton(text='1 км', callback_data='1km')
r_2 = InlineKeyboardButton(text='2.5 км', callback_data='2.5km')
r_3 = InlineKeyboardButton(text='5 км', callback_data='5km')
r_4 = InlineKeyboardButton(text='10 км', callback_data='10km')
kb_r = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(r_1, r_2, r_3, r_4)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('ку', reply_markup=kb_inl)


@dp.callback_query_handler(text=['startg'])
async def choose_i_beam(call: types.CallbackQuery):
    await call.message.answer('Отправьте местоположение:', reply_markup=loc_req)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.message_handler(content_types=['location'])
async def handle_loc(message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['loc_u'] = message.location
        await message.answer('Готово', reply_markup=types.ReplyKeyboardRemove())
        await message.answer('Выберите радиус до:', reply_markup=kb_r)


@dp.callback_query_handler(text=['1km'])
async def km1(call: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        q = str(data['loc_u'])
        w = json.loads(q)
        sh_g_1km = 0.00899807667  # градусов широты в около 1км
        dolg_g_1km = 0.00899807667  # градусов долготы в около 1км
        im_dot = [w['latitude'], w['longitude']]
        kmm = 1
        shp = im_dot[0] + sh_g_1km * kmm
        shm = im_dot[0] - sh_g_1km * kmm
        dpp = im_dot[1] + dolg_g_1km * kmm
        dm = im_dot[1] - dolg_g_1km * kmm
        sh = round(random.uniform(shm, shp), 5)
        d = round(random.uniform(dm, dpp), 5)
        await bot.send_location(chat_id=call.from_user.id, latitude=sh, longitude=d)
        await call.message.answer(f'{sh}, {d}')
        await call.message.answer(f'Иди, радиус до {kmm} км')
        await state.finish()


@dp.callback_query_handler(text=['2.5km'])
async def km25(call: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        q = str(data['loc_u'])
        w = json.loads(q)
        sh_g_1km = 0.00899807667  # градусов широты в около 1км
        dolg_g_1km = 0.00899807667  # градусов долготы в около 1км
        im_dot = [w['latitude'], w['longitude']]
        kmm = 2.5
        shp = im_dot[0] + sh_g_1km * kmm
        shm = im_dot[0] - sh_g_1km * kmm
        dpp = im_dot[1] + dolg_g_1km * kmm
        dm = im_dot[1] - dolg_g_1km * kmm
        sh = round(random.uniform(shm, shp), 5)
        d = round(random.uniform(dm, dpp), 5)
        await bot.send_location(chat_id=call.from_user.id, latitude=sh, longitude=d)
        await call.message.answer(f'{sh}, {d}')
        await call.message.answer(f'Иди, радиус до {kmm} км')
        await state.finish()


@dp.callback_query_handler(text=['5km'])
async def km5(call: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        q = str(data['loc_u'])
        w = json.loads(q)
        sh_g_1km = 0.00899807667  # градусов широты в около 1км
        dolg_g_1km = 0.00899807667  # градусов долготы в около 1км
        im_dot = [w['latitude'], w['longitude']]
        kmm = 5
        shp = im_dot[0] + sh_g_1km * kmm
        shm = im_dot[0] - sh_g_1km * kmm
        dpp = im_dot[1] + dolg_g_1km * kmm
        dm = im_dot[1] - dolg_g_1km * kmm
        sh = round(random.uniform(shm, shp), 5)
        d = round(random.uniform(dm, dpp), 5)
        await bot.send_location(chat_id=call.from_user.id, latitude=sh, longitude=d)
        await call.message.answer(f'{sh}, {d}')
        await call.message.answer(f'Иди, радиус до {kmm} км')
        await state.finish()


@dp.callback_query_handler(text=['10km'])
async def km5(call: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        q = str(data['loc_u'])
        w = json.loads(q)
        sh_g_1km = 0.00899807667  # градусов широты в около 1км
        dolg_g_1km = 0.00899807667  # градусов долготы в около 1км
        im_dot = [w['latitude'], w['longitude']]
        kmm = 10
        shp = im_dot[0] + sh_g_1km * kmm
        shm = im_dot[0] - sh_g_1km * kmm
        dpp = im_dot[1] + dolg_g_1km * kmm
        dm = im_dot[1] - dolg_g_1km * kmm
        sh = round(random.uniform(shm, shp), 5)
        d = round(random.uniform(dm, dpp), 5)
        await bot.send_location(chat_id=call.from_user.id, latitude=sh, longitude=d)
        await call.message.answer(f'{sh}, {d}')
        await call.message.answer(f'Иди, радиус до {kmm} км')
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)