import logging
import os

import requests
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from json import JSONDecoder, decoder

from utils.json_to_html import convert_to_text
from services.finance_site import fin_service

from states.bot_state import UserState

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ["API_TOKEN"])
dp = Dispatcher(bot, storage=MemoryStorage())
PERKS = ["Admin user", "Casual user", "Master user"]

async def startup(_):
    response = requests.get("http://127.0.0.1:8000/api/ping/")
    response.raise_for_status()

@dp.message_handler(commands=['start'])
async def get_start(msg: types.Message):
    telegram_id = msg["from"]["id"]
    first_name = msg["from"]["first_name"]
    last_name = msg["from"]["last_name"]
    if first_name and last_name:
        username = first_name + " " + last_name
    elif first_name:
        username = first_name
    else:
        username = msg['from']['username']
    nickname = msg['from']['username']
    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_kb.add(types.InlineKeyboardButton(f"{username}", callback_data=f"start :{username}:{telegram_id}"))
    inline_kb.add(types.InlineKeyboardButton(f"{nickname}", callback_data=f"start :{nickname}:{telegram_id}"))
    await msg.answer(f"Добро пожаловать в Finance_Bot\nКак я могу вас называть?\n\n{username}\nили\n{nickname}", reply_markup=inline_kb)


@dp.callback_query_handler(Text(contains="start"))
async def get_admin_commands(callback: types.CallbackQuery):
    username = callback['data'].split(":")[1]
    telegram_id = callback['data'].split(":")[2]
    user = fin_service.create_user({"username": username, "telegram_id": telegram_id})
    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_kb.add(types.InlineKeyboardButton("нажмите для продолжения", callback_data="menu"))
    await callback.message.edit_text("...Одно мгновение...", reply_markup=inline_kb)

@dp.callback_query_handler(Text(contains="menu"))
async def get_admin_commands(callback: types.CallbackQuery):

    users_spaces = fin_service.add_event


    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_kb.add(types.InlineKeyboardButton("Get users", callback_data="get_users_1"))
    await callback.message.edit_text("Добро пожаловать в меню", reply_markup=inline_kb)

# # @dp.callback_query_handler(Text(contains="get_users"))
# # async def display_users(callback: types.CallbackQuery, state:FSMContext):
# #     await state.finish()

# #     page = int(callback.data.split("_")[-1])
# #     users_response = event_service.get_users(page)

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)

# #     for user in users_response["results"]:
# #         inline_kb.add(
# #             types.InlineKeyboardButton(f"{user['id']}. {user['username']}", callback_data=f"get_user:{user['id']}")
# #         )

# #     pagination_buttons = []

# #     if users_response["previous"]:
# #         pagination_buttons.append(types.InlineKeyboardButton("⬅️👹😈", callback_data=f"get_users_{page - 1}"))
# #     if users_response["next"]:
# #         pagination_buttons.append(types.InlineKeyboardButton("😈👹➡️", callback_data=f"get_users_{page + 1}"))

# #     await callback.message.edit_text("Edited", reply_markup=inline_kb.row(*pagination_buttons))


# # @dp.callback_query_handler(Text(contains="get_user:"))
# # async def display_user(callback: types.CallbackQuery, state:FSMContext):
# #     user_id = int(callback.data.split(":")[-1])
# #     user = event_service.get_user(user_id)


# #     await state.set_state(UserState.user_state.state)
# #     await state.update_data(user, msg_id=callback.message.message_id)
# #     # print(await state.get_data())

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)
# #     inline_kb.add(types.InlineKeyboardButton(f"user id: {user_id}", callback_data=f"user_id:{user_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"first name: {user['first_name']}", callback_data=f"user_id:{user_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"last name: {user['last_name']}", callback_data=f"user_id:{user_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"user name: {user['username']}", callback_data="change_username"))
# #     inline_kb.add(types.InlineKeyboardButton("password: *****", callback_data="change_password"))
# #     inline_kb.add(types.InlineKeyboardButton(f"e-mail: {user['email']}", callback_data=f"user_id:{user_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"tier: {user['tier_field']}", callback_data="change_tier"))


# #     await callback.message.edit_text("Edited", reply_markup=inline_kb)


# # @dp.callback_query_handler(Text(equals="change_tier"), state=UserState.user_state)
# # async def choose_tier (callback: types.CallbackQuery, state:FSMContext):

# #     await state.set_state(UserState.tier_state.state)

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)

# #     for tier in TIERS:
# #         inline_kb.add(types.InlineKeyboardButton(f"{tier}", callback_data=f"tier:{tier}"))
    

# #     await callback.message.edit_text("Tier сhosen", reply_markup=inline_kb)


# # @dp.callback_query_handler(Text(contains="tier:"), state=UserState.tier_state)
# # async def chenge_tier (callback: types.CallbackQuery, state:FSMContext):
# #     tier_fields = callback.data.split(":")[-1]
# #     tier = tier_fields[0]
# #     data = await state.get_data()
# #     user = event_service.update_user(data['id'], {"tier_field": tier_fields, "tier": tier})

# #     await state.finish()

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)

# #     await callback.message.edit_text("tier сhosen", reply_markup=inline_kb)


# # @dp.callback_query_handler(Text(equals="change_username"), state=UserState.user_state)
# # async def change_username (callback: types.CallbackQuery, state:FSMContext):

# #     await state.set_state(UserState.username_state.state)
# #     msg = await callback.message.answer("Type new username")
# #     await state.update_data(msg_to_delete=msg.message_id, msg_id=callback.message.message_id)

# # @dp.message_handler(state=UserState.username_state)
# # async def chenge_user_name (msg: types.Message, state:FSMContext):
# #     username = msg.text.strip()
# #     data = await state.get_data()
# #     user = event_service.update_user(data['id'], {"username": username})
# #     msg_text = convert_to_text(user)
# #     await msg.answer("success")
# #     await state.finish()


# # @dp.callback_query_handler(Text(equals="change_password"), state=UserState.user_state)
# # async def change_password (callback: types.CallbackQuery, state:FSMContext):

# #     await state.set_state(UserState.password_state.state)
# #     msg = await callback.message.answer("Type new password")
# #     await state.update_data(msg_to_delete=msg.message_id, msg_id=callback.message.message_id)

# # @dp.message_handler(state=UserState.password_state)
# # async def chenge_password_s2 (msg: types.Message, state:FSMContext):
# #     password = msg.text.strip()
# #     data = await state.get_data()
# #     user = event_service.update_user(data['id'], {"password": password})
# #     await msg.answer("success")
# #     await state.finish()




# # @dp.callback_query_handler(Text(contains="get_events"))
# # async def display_events(callback: types.CallbackQuery, state:FSMContext):
# #     await state.finish()

# #     page = int(callback.data.split("_")[-1])
# #     events_response = event_service.get_events(page)

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)

# #     # JSONDecoder.decode(events_response, dict)

# #     print(events_response)
# #     types.InlineKeyboardButton(f"{event['id']}. {event['title']}", callback_data=f"get_event:{event['id']}")
# #     for event in events_response.get('data'):
# #         # print(event)
# #         inline_kb.add(
# #             types.InlineKeyboardButton(f"{event['id']}. {event['title']}", callback_data=f"get_event:{event['id']}")
# #         )

# #     inline_kb.add(types.InlineKeyboardButton(f"add event:{event['id']}", callback_data=f"add_event:{event['id']}"))

# #     pagination_buttons = []

# #     if events_response["previous"]:
# #         pagination_buttons.append(types.InlineKeyboardButton("⬅️👹😈", callback_data=f"get_events_{page - 1}"))
# #     if events_response["next"]:
# #         pagination_buttons.append(types.InlineKeyboardButton("😈👹➡️", callback_data=f"get_events_{page + 1}"))

# #     await callback.message.edit_text("Edited", reply_markup=inline_kb.row(*pagination_buttons))


# # @dp.callback_query_handler(Text(contains="get_event:"))
# # async def display_event(callback: types.CallbackQuery, state:FSMContext):
# #     event_id = int(callback.data.split(":")[-1])
# #     event = event_service.get_event(event_id)

# #     await state.set_state(UserState.event_state.state)
# #     await state.update_data(event, msg_id=callback.message.message_id)

# #     inline_kb = types.InlineKeyboardMarkup(row_width=1)
# #     inline_kb.add(types.InlineKeyboardButton(f"event id: {event_id}", callback_data=f"event_id:{event_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"title: {event['title']}", callback_data=f"title:{event_id}"))
# #     inline_kb.add(types.InlineKeyboardButton(f"date: {event['date']}", callback_data=f"date:{event_id}"))

# #     await callback.message.edit_text("Edited", reply_markup=inline_kb)


# @dp.callback_query_handler(Text(equals="add_event"))
# async def add_event_s0(callback: types.CallbackQuery, state:FSMContext):
#     await state.set_state(UserState.event_state.state)
#     msg = await callback.message.answer("Type data")

# @dp.message_handler(state=UserState.event_state)
# async def add_event_s1 (msg: types.Message, state:FSMContext):
#     mesg = msg.text.strip()

#     await msg.answer("Type title")
#     await state.set_state(UserState.event_state_2.state)
#     # await state.update_data(msg, msg_id=msg.message_id)

#     await state.update_data(msg_to_delete=msg.message_id, msg_id=msg.message_id)

# @dp.callback_query_handler(state=UserState.event_state_2)
# async def add_event_s2 (callback: types.CallbackQuery, state:FSMContext):


#     # event = event_service.add_event({"title": title, "date": date})

#     msg2 = await callback.message.answer("Type data")

#     await state.update_data(msg2)

#     await state.update_data(msg_to_delete=msg2.message_id, msg_id=callback.message.message_id)

# @dp.callback_query_handler(state=UserState.event_state_2)
# async def add_event_s3 (callback: types.CallbackQuery, state:FSMContext):
#     # event = event_service.add_event({"title": title, "date": date})
#     await print(state.get_data())


executor.start_polling(dp, skip_updates=True, on_startup=startup)