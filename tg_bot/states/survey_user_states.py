from telebot.handler_backends import State, StatesGroup

from telebot.storage import StateMemoryStorage


state_storage = StateMemoryStorage()


class MyStates(StatesGroup):
    id = State()
    name = State()
    surname = State()
    age = State()