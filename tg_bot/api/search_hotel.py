import random

from logger import logger
from telebot.types import InputMediaPhoto

from tg_bot import api
from tg_bot.config_data.config import url_hotels
from tg_bot.loader import bot, db_history


def find_and_show_hotels(message, data):
    """
    Формирование запросов на поиск отелей, и детальной информации о них (адрес, фотографии).
    Вывод полученных данных пользователю в чат.
    : param message : Message
    : param data : Dict данные, собранные от пользователя
    : return : None
    """
    payload = {"currency": "USD", "search_type": "CITY", "dest_id": f"{data['destination_id']}",
               "arrival_date": f"{data['checkInDate']['year']}-{data['checkInDate']['month']}-{data['checkInDate']['day']}",
               "departure_date": f"{data['checkOutDate']['year']}-{data['checkOutDate']['month']}-{data['checkOutDate']['day']}",
               "price_min": f"{data['price_min']}", "price_max": f"{data['price_max']}"}

    # Отправка запроса серверу на поиск отелей
    response_hotels = api.request_api.request('GET', url_hotels, payload)
    logger.info(response_hotels.text)
    logger.info(f'Сервер вернул ответ {response_hotels.status_code}. User_id: {message.chat.id}')
    # Если сервер возвращает статус-код не 200, то все остальные действия будут бессмысленными.
    if response_hotels.status_code == 200:
        # Обработка полученного ответа от сервера и формирование отсортированного словаря с отелями
        hotels = api.city_api.get_hotel_id(response_text=response_hotels.text, command=data['command'],
                                           min_rate=int(data["min_rate"]), max_rate=int(data["max_rate"]),
                                           count=int(data["quantity_hotels"]))

        if 'error' in hotels:
            bot.send_message(message.chat.id, hotels['error'])
            bot.send_message(message.chat.id, 'Попробуйте осуществить поиск с другими параметрами')
            bot.send_message(message.chat.id, '')

            # Нужен дополнительный запрос, чтобы получить детальную информацию об отеле.  # Цикл будет выполняться, пока не достигнет числа отелей, которое запросил пользователь.

        db_history.set_data(message.chat.id, data)
        medias = []
        links_to_images = []
        for hotel in hotels.values():
            try:

                for random_url in range(int(data['photo_count'])):
                    links_to_images.append(hotel['photo'][random.randint(0, len(hotel['photo']) - 1)])
            except IndexError:
                continue  # Если количество фотографий > 0: создаем медиа группу с фотками и выводим ее в чат
        if int(data['photo_count']) > 0:
            # формируем MediaGroup с фотографиями и описанием отеля и посылаем в чат
            for number, url in enumerate(links_to_images, 1):
                medias.append(InputMediaPhoto(media=url))
            if len(medias) > 10:
                start = 0
                medias_length = len(medias)
                batch_size = 10
                while start < medias_length:
                    end = min(start + batch_size, medias_length)
                    batch = medias[start:end]
                    bot.send_media_group(message.chat.id, batch)
                    start += batch_size
            else:
                bot.send_media_group(message.chat.id, medias)
            logger.info(f"Выдаю найденную информацию в чат. User_id: {message.chat.id}")
        # если фотки не нужны, то просто выводим данные об отеле
        logger.info(f"Выдаю найденную информацию в чат. User_id: {message.chat.id}")
        answer = ''
        for i_hotel in hotels.values():
            answer += f"{i_hotel['name']} цена - {i_hotel['price']} рейтинг - {i_hotel['rating']}\n"
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, f'Что-то пошло не так, код ошибки: {response_hotels.status_code}')
    logger.info(f"Поиск окончен. User_id: {message.chat.id}")
    bot.send_message(message.chat.id, 'Поиск окончен!')
    bot.set_state(message.chat.id, None)


def print_data(message, data):
    """
    Выводим в чат всё, что собрали от пользователя и передаем это в функцию поиска
    отелей.
    : param message : Message
    : param data: Dict данные собранные от пользователя
    : return : None
    """
    # Отправляем в базу данных собранные данные, а там уже выберу что нужно
    logger.info(f'Вывод суммарной информации о параметрах запроса пользователем. User_id: {message.chat.id}')
    text_message = ('Исходные данные:\n'
                    f'Дата и время запроса: {data["date_time"]}\n'
                    f'Введена команда: {data["command"]}\n'
                    f'Вы ввели город: {data["input_city"]}\n'
                    f'Выбран город с id: {data["destination_id"]}\n'
                    f'Количество отелей: {data["quantity_hotels"]}\n'
                    f'Минимальная цена: {data["price_min"]}\n'
                    f'Максимальная цена: {data["price_max"]}\n'
                    f'Нужны ли фотографии? {data["photo_need"]}\n'
                    f'Количество фотографий: {data["photo_count"]}\n'
                    f'Дата заезда: {data["checkInDate"]["day"]}-'
                    f'{data["checkInDate"]["month"]}-{data["checkInDate"]["year"]}\n'
                    f'Дата выезда: {data["checkOutDate"]["day"]}-'
                    f'{data["checkOutDate"]["month"]}-{data["checkOutDate"]["year"]}\n')
    if data['sort'] == 'RATING':
        bot.send_message(message.chat.id, text_message + f'Минимальный рейтинг: {data["min_rate"]}\n'
                                                         f'Максимальный рейтинг: {data["max_rate"]}')
    else:
        bot.send_message(message.chat.id, text_message)
    find_and_show_hotels(message, data)
