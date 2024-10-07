from telebot.types import Message

from tg_bot.api.city_api import get_api_data, get_api_city
from tg_bot.loader import bot
from tg_bot.states.info_states import UserState

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введи название города на латинице')
    bot.set_state(message.from_user.id,UserState.checkIn)

@bot.message_handler(state=UserState.checkIn)
def get_checkIn(messsage: Message) -> None:
    bot.send_message(messsage.from_user.id, 'Введите дату заселения (ДД-ММ-ГГГГ):')
    bot.set_state(messsage.from_user.id,UserState.checkOut)

@bot.message_handler(state=UserState.checkOut)
def get_checkOut(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Введите дату выселения (ДД-ММ-ГГГГ):')




def get_city(message):
    city = message.text.strip().lower()
    city_inf = get_api_city(f'{city}')
    #city_json = city_inf.json()
    hotel_res = get_api_data(city_inf, get_api_city)
    bot.reply_to(message, f'Список отелей:{hotel_res}')


def get_data(message):
    bot.send_message(message.chat.id, 'Введи дату заселения в формате: yyyy-mm-dd')
    checkIn = message.text.strip()
    print(checkIn)



