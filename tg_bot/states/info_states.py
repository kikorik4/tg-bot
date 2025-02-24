from telebot import State
from telebot.states import StatesGroup


class HistoryState(StatesGroup):
    count = State()

