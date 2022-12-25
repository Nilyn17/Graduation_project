from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    user_state = State()
    tier_state = State()
    username_state = State()
    password_state = State()
    event_state = State()
    event_state_2 = State()