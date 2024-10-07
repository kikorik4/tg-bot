from telebot import State
from telebot.states import StatesGroup


class UserState(StatesGroup):
    city = State()
    checkIn = State()
    checkOut = State()

