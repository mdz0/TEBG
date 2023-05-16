import random
import json
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings_control.stg_ctrl import readConfig
from bot.variables import *
from bot.keyboard import *


def botBody():
    bot = Bot(token=readConfig())
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):
        await message.answer('Готовы к путешествию?', reply_markup=kb_inl)

    @dp.callback_query_handler(text=['startg'])
    async def choose_i_beam(call: types.CallbackQuery):
        await call.message.answer('Отправьте местоположение:', reply_markup=loc_req)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    @dp.message_handler(content_types=['location'])
    async def handle_loc(message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['loc_u'] = message.location
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.answer('Выберите радиус до:', reply_markup=kb_r)

    @dp.callback_query_handler(text=['1km'])
    async def km1(call: types.CallbackQuery, state: FSMContext) -> None:
        async with state.proxy() as data:
            q = str(data['loc_u'])
            w = json.loads(q)
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
            await call.message.answer(f'Радиус до {kmm} км. Удачного пути!')
            await state.finish()
            await call.message.answer('Готовы к новому путешествию?', reply_markup=kb_inl)

    @dp.callback_query_handler(text=['2.5km'])
    async def km25(call: types.CallbackQuery, state: FSMContext) -> None:
        async with state.proxy() as data:
            q = str(data['loc_u'])
            w = json.loads(q)
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
            await call.message.answer(f'Радиус до {kmm} км. Удачного пути!')
            await state.finish()
            await call.message.answer('Готовы к новому путешествию?', reply_markup=kb_inl)

    @dp.callback_query_handler(text=['5km'])
    async def km5(call: types.CallbackQuery, state: FSMContext) -> None:
        async with state.proxy() as data:
            q = str(data['loc_u'])
            w = json.loads(q)
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
            await call.message.answer(f'Радиус до {kmm} км. Удачного пути!')
            await state.finish()
            await call.message.answer('Готовы к новому путешествию?', reply_markup=kb_inl)

    @dp.callback_query_handler(text=['10km'])
    async def km5(call: types.CallbackQuery, state: FSMContext) -> None:
        async with state.proxy() as data:
            q = str(data['loc_u'])
            w = json.loads(q)
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
            await call.message.answer(f'Радиус до {kmm} км. Удачного пути!')
            await state.finish()
            await call.message.answer('Готовы к новому путешествию?', reply_markup=kb_inl)

    executor.start_polling(dp, skip_updates=True)
