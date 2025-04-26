import datetime

from logger import logger
from telebot.types import Message

from tg_bot import api
from tg_bot import keyboards
from tg_bot.config_data.config import url_city
from tg_bot.handlers.callback_handler import photo_need
from tg_bot.keyboards.inline.inline_calendar.calendar_inline import Calendar
from tg_bot.loader import bot
from tg_bot.states.info_states import UserInputState


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def low_high_best_handler(message: Message) -> None:
    """
        Обработчик команд, срабатывает на три команды /lowprice, /highprice, /bestdeal
        и запоминает необходимые данные. Спрашивает пользователя - какой искать город.
        : param message : Message
        : return : None
        """
    bot.set_state(message.chat.id, UserInputState.command)
    with bot.retrieve_data(message.chat.id) as data:
        data.clear()
        logger.info('Запоминаем выбранную команду: ' + message.text + f" User_id: {message.chat.id}")
        data['command'] = message.text
        data['sort'] = check_command(message.text)
        data['date_time'] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        data['chat_id'] = message.chat.id
    bot.set_state(message.chat.id, UserInputState.input_city)
    bot.send_message(message.from_user.id, f"Введите город в котором нужно найти отель (на латинице): ")


@bot.message_handler(state=UserInputState.input_city)
def input_city(message: Message) -> None:
    """
        Ввод пользователем города и отправка запроса серверу на поиск города.
        : param message : Message
        : return : None
        """
    with bot.retrieve_data(message.chat.id) as data:
        data['input_city'] = message.text
        logger.info('Пользователь ввел город: ' + message.text + f' User_id: {message.chat.id}')
        querystring = {"query": message.text}
        response_cities = api.request_api.request('GET', url_city, querystring)
        if response_cities.status_code == 200:
            logger.info('Сервер ответил: ' + str(response_cities.status_code) + f' User_id: {message.chat.id}')
            city_dest_id = api.city_api.get_city_id(response_cities.json())
            data['destination_id'] = city_dest_id
            bot.set_state(message.chat.id, UserInputState.quantity_hotels)
            bot.send_message(message.chat.id, f'Сколько отелей вывести?')
        else:
            bot.send_message(message.chat.id, f"Что-то пошло не так, код ошибки: {response_cities.status_code}")
            bot.send_message(message.chat.id, 'Нажмите команду еще раз. И введите другой город.')
            data.clear()


@bot.message_handler(state=UserInputState.quantity_hotels)
def input_quantity(message: Message) -> None:
    """
       Ввод количества выдаваемых на странице отелей, а так же проверка, является ли
       введённое числом и входит ли оно в заданный диапазон от 1 до 25
       : param message : Message
       : return : None
       """
    if message.text.isdigit():
        if 0 < int(message.text) <= 25:
            with bot.retrieve_data(message.chat.id) as data:
                data['quantity_hotels'] = message.text
            bot.set_state(message.chat.id, UserInputState.priceMin)
            bot.send_message(message.chat.id, f'Введите минимальную стоимость отеля в долларах США:')
        else:
            bot.send_message(message.chat.id, 'Ошибка! Это должно быть число в диапазоне от 1 до 500! Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.priceMin)
def input_price_min(message: Message) -> None:
    """
    Ввод минимальной стоимости отеля и проверка чтобы это было число.
    : param message : Message
    : return : None
    """
    if message.text.isdigit():
        logger.info('Ввод и запись минимальной стоимости отеля: ' + message.text + f' User_id: {message.chat.id}')
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.chat.id, UserInputState.priceMax)
        bot.send_message(message.chat.id, f'Введите максимальную стоимость отеля в долларах США:')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.priceMax)
def input_price_max(message: Message) -> None:
    """
    Ввод максимальной стоимости отеля и проверка чтобы это было число. Максимальное число не может
    быть меньше минимального.
    : param message : Message
    : return : None
    """
    if message.text.isdigit():
        logger.info(
            'Ввод и запись максимальной стоимости отеля, сравнение с price_min: ' + message.text + f' User_id: {message.chat.id}')
        with bot.retrieve_data(message.chat.id) as data:
            if int(data['price_min']) < int(message.text):
                data['price_max'] = message.text
                call = keyboards.inline.all_buttons.show_buttons_photo_need_yes_no(message)
                photo_need.need_photo_callback(call)
            else:
                bot.send_message(message.chat.id, 'Максимальная цена должна быть больше минимальной. Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.photo_count)
def input_photo_quantity(message: Message) -> None:
    """
    Ввод количества фотографий и проверка на число и на соответствие заданному диапазону от 1 до 10
    : param message : Message
    : return : None
    """
    if message.text.isdigit():
        if 0 < int(message.text) <= 10:
            logger.info('Ввод и запись количества фотографий: ' + message.text + f' User_id: {message.chat.id}')
            with bot.retrieve_data(message.chat.id) as data:
                data['photo_count'] = message.text
            my_calendar(message, 'заезда')
        else:
            bot.send_message(message.chat.id, 'Число фотографий должно быть в диапазоне от 1 до 10! Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.min_rate)
def input_min_rate(message: Message) -> None:
    """
    Ввод минимального рейтинга
    : param message : Message
    : return : None
    """
    if message.text.isdigit():
        logger.info('Ввод и запись начала диапазона от центра: ' + message.text + f' User_id: {message.chat.id}')
        with bot.retrieve_data(message.chat.id) as data:
            data['min_rate'] = message.text
        bot.set_state(message.chat.id, UserInputState.max_rate)
        bot.send_message(message.chat.id, f'Введите максимальный рейтинг: ')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.max_rate)
def input_max_rate(message: Message) -> None:
    """
    Ввод максимального рейтинга
    : param message : Message
    : return : None
    """
    if message.text.isdigit():
        logger.info('Ввод и запись конца диапазона от центра: ' + message.text + f' User_id: {message.chat.id}')
        with bot.retrieve_data(message.chat.id) as data:
            data['max_rate'] = message.text
            api.search_hotel.print_data(message, data)
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


def check_command(command: str) -> str:
    """
        Проверка команды и назначение параметра сортировки
        : param command : str команда, выбранная (введенная) пользователем
        : return : str команда сортировки
        """
    if command == '/bestdeal':
        return 'RATING'
    elif command == '/lowprice' or command == '/highprice':
        return 'PRICE_LOW_TO_HIGH'


bot_calendar = Calendar()


def my_calendar(message: Message, word: str) -> None:
    """
        Запуск инлайн-клавиатуры (календаря) для выбора дат заезда и выезда
        : param message : Message
        : param word : str слово (заезда или выезда)
        : return : None
        """
    logger.info(f'Вызов календаря {word}. User_id: {message.chat.id}')
    bot.send_message(message.chat.id, f'Выберите дату: {word}', reply_markup=bot_calendar.create_calendar())
