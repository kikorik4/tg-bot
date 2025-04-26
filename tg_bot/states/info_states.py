from telebot import State
from telebot.states import StatesGroup


class HistoryState(StatesGroup):
    count = State()


class UserInputState(StatesGroup):
    command = State()
    input_city = State()
    destinationId = State()
    quantity_hotels = State()
    photo_count = State()
    input_date = State()
    priceMin = State()
    priceMax = State()
    min_rate = State()
    max_rate = State()
