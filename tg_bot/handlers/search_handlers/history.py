import json

from logger import logger

from tg_bot.handlers.search_handlers.filter import for_history
from tg_bot.keyboards.inline.delete_history import get_clean_button
from tg_bot.loader import bot, db_history
from tg_bot.states.info_states import HistoryState


@bot.message_handler(commands=['history'])
def start_history(message) -> None:
    """
        Начало истории
        """
    logger.info(f'user_id: {message.from_user.id}')
    bot.send_message(message.chat.id, 'Сколько последних запросов Вам показать?(Не более 10)',
                     reply_markup=get_clean_button())
    bot.set_state(message.from_user.id, HistoryState.count, message.chat.id)


@bot.message_handler(state=HistoryState.count, is_digit=True, count_digit=True)
def get_history(message):
    """
    Вывод истории поиска
    """
    answer = ''
    data = db_history.get_data(message.chat.id, message.text)
    rows = data.fetchall()
    logger.info(rows)
    if rows:
        for row in rows:
            id = row[0]
            command = row[1]
            if command == 'survey':
                info = json.loads(row[2])
                name, surname, age = info['name'], info['surname'], info['age']
                answer = f'id: {id}\ncommand: {command}\nname: {name}\nsurname: {surname}\nage: {age}\n'
                bot.send_message(message.chat.id, answer)
            elif command == '/start' or '/bestdeal' or '/lowprice' or '/highprice':
                input_city = row[2]
                destination_id = row[3]
                photo_need = row[4]
                answer = f'id: {id}\ncommand: {command}\ninput_city: {input_city}\ndestination_id: {destination_id}\nphoto_need: {photo_need}'
                bot.send_message(message.chat.id, answer)


@bot.callback_query_handler(func=None, history_config=for_history.filter(clean='Очистить'))
def clean_history(call):
    db_history.del_data(call.from_user.id)
    bot.send_message(call.message.chat.id, 'История очищена')


@bot.message_handler(state=HistoryState.count, is_digit=False)
def bad_digit(message):
    """
        :param message: не число
        """
    logger.error('Какой-то числовой эрор')
    bot.send_message(message.chat.id, 'Введите число больше 0')


@bot.message_handler(state=HistoryState.count, is_digit=True, count_digit=False)
def many_count(message):
    """
        не тот диапазон
        """
    logger.error('Какой-то числовой эрор')
    bot.send_message(message.chat.id, 'Введите число в диапазоне от 1 до 10')
