from tg_bot.api.city_api import get_city_id, send_hotel_result, get_hotel_id
from tg_bot.loader import bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введи название города на латинице')

@bot.message_handler(content_types=['text'])
def get_city(message):
    city = message.text.strip().lower()
    city_inf = get_city_id(f'{city}')
    city_json = city_inf.json()
    hotel_res = send_hotel_result(city_json, get_hotel_id)
    bot.reply_to(message, f'Список отелей:{hotel_res}')
