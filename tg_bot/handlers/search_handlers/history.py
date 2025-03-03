import json

from logger import logger
from tg_bot.loader import bot, db_history
from tg_bot.states.info_states import HistoryState


@bot.message_handler(commands=['history'])
def start_history(message):
    bot.send_message(message.chat.id, 'Сколько последних запросов Вам показать?(Не более 10)')
    bot.set_state(message.from_user.id, HistoryState.count, message.chat.id)

@bot.message_handler(state=HistoryState.count, is_digit=True, count_digit=True)
def get_history(message):
    data = db_history.get_data(message.from_user.id, message.text)
    rows = data.fetchall()
    if rows:
        for i_row in rows:
            data, command, hotels = i_row[0], i_row[1], json.loads(i_row[2])
            bot.send_message(message.chat.id, f'{data} выполнили команду {command} и нашли: ')
            for _ in range(len(hotels)):
                for id, name in hotels.items():
                    bot.send_message(message.chat.id, f'{name}')

@bot.message_handler(state=HistoryState.count, is_digit=False)
def bad_digit(message):
    logger.error('Какой-то числовой эрор')
    bot.send_message(message.chat.id, 'Введите число больше 0')


@bot.message_handler(state=HistoryState.count, is_digit=True, count_digit=False)
def many_count(message):
    logger.error('Какой-то числовой эрор')
    bot.send_message(message.chat.id, 'Введите число в диапазоне от 1 до 10')