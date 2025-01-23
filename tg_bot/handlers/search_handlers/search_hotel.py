from pyexpat.errors import messages
from datetime import datetime
from telebot.types import Message

from tg_bot.api.city_api import send_hotel_result, get_city_id, get_hotel_id
from tg_bot.loader import bot
from tg_bot.states.info_states import UserState

information = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, 'Привет! Введи название города на латинице')
    city = message.text.strip()
    information[chat_id] = {}
    bot.register_next_step_handler(message,save_city)
#    bot.set_state(message.from_user.id,UserState.checkIn)
    with bot.retrieve_data(message.from_user.id) as data:
        data['city'] = {'city': city}

def save_city(message):
    chat_id = message.chat.id
    city = message.text.strip().lower()
    information[chat_id]['city'] = city
    bot.send_message(chat_id, 'Введите дату заселения (ДД-ММ-ГГГГ):')
    bot.register_next_step_handler(message, save_check_In)

#@bot.message_handler(state=UserState.checkIn)
#def get_checkIn(messsage: Message) -> None:
    #chat_id = messsage.chat.id
    #bot.send_message(messsage.from_user.id, 'Введите дату заселения (ДД-ММ-ГГГГ):')
   # bot.register_next_step_handler(chat_id)
   # bot.set_state(messsage.from_user.id,UserState.checkOut)

def save_check_In(message):
    chat_id = message.chat.id
    check_in = message.text
    check_in_data = datetime.strptime(check_in, '%d-%m-%Y')
    checkIn_data = check_in_data.strftime('%Y-%m-%d')
    information[chat_id]['checkIn'] = checkIn_data
    bot.send_message(chat_id, 'Введите дату выселения (ДД-ММ-ГГГГ):')
    bot.register_next_step_handler(message, save_check_Out)


#@bot.message_handler(state=UserState.checkOut)
#def get_checkOut(message: Message) -> None:
 #   chat_id = message.chat.id
  #  bot.send_message(message.from_user.id, 'Введите дату выселения (ДД-ММ-ГГГГ):')
   # bot.register_next_step_handler(chat_id)

def save_check_Out(message):
    chat_id = message.chat.id
    check_out = message.text
    check_out_data = datetime.strptime(check_out,'%d-%m-%Y')
    checkOut_data = check_out_data.strftime('%Y-%m-%d')
    information[chat_id]['checkOut'] = checkOut_data
    city = information[chat_id]['city']
    check_in = information[chat_id]['checkIn']
    check_out = information[chat_id]['checkOut']
    bot.send_message(chat_id,
                     f'Введенная инфомация:\nГород: {city}\nДата заселения: {check_in}\nДата выселения: {check_out}')
    result = get_city(message)


def get_city(message):
    chat_id = message.chat.id
    city = information[chat_id]['city']
    city_inf = get_city_id(f'{city}')
    city_json = city_inf.json()
    hotel_res = send_hotel_result(city_json, information[chat_id]['checkIn'],
                                 information[chat_id]['checkOut'], get_hotel_id)
    bot.send_message(chat_id, f'Список отелей:{hotel_res}')



#def get_data(message):
   # bot.send_message(message.chat.id, 'Введи дату заселения в формате: yyyy-mm-dd')
   # checkIn = message.text.strip()
    #print(checkIn)



