from typing import Dict

import json

def get_city_id(response_text):
    """
    Принимает ответ от сервера с информацией о городе. Возвращает id
    города.
    :param response_text: str текстовая строка, ответ от сервера
    :return:str возвращает id города
    """
    if not response_text:
        raise LookupError('Запрос пуст...')
    try:
        dest_id = response_text['data'][0]['dest_id']
    except KeyError:
        pass
    return dest_id


def get_hotel_id(response_text: str, command: str, min_rate: int, max_rate: int, count) -> Dict:
    """
    Принимает ответ от сервера, выбранную команду сортировки, количество отелей, а так же минимальный и максимальный рейтинг. Возвращает отсортированный словарь, в зависимости от команды сортировки.
    :param response_text: Ответ от сервера, в котором содержится информация об отелях
    :param command: Команда сортировки
    :param min_rate: Минимальный рейтинг
    :param max_rate: Максимальный рейтинг
    :param count: Количество отелей
    :return: Dict Возвращает словарь с данными об отелях
    """
    data = json.loads(response_text)
    if not data:
        raise LookupError('Запрос пуст...')
    if 'errors' in data.keys():
        return {'error': data['errors'][0]['message']}
    hotels_data = {}
    for num, hotel in enumerate(data['data']['hotels'], 1):
        try:
            if num <= count:
                hotels_data[hotel['property']['name']] = {
                'name': hotel['property']['name'],
                'id': hotel['hotel_id'],
                'rating': hotel['property']['reviewScore'],
                'price': round(hotel['property']['priceBreakdown']['grossPrice']['value']),
                'photo': hotel['property']['photoUrls']}

        except (KeyError, TypeError):
            continue
    if command == '/highprice':
        hotels_data = {
            key: value for key, value in
            sorted(hotels_data.items(), key=lambda hotel_id: hotel_id[1]['price'], reverse=True)}

    elif command == '/lowprice':
        hotels_data = {
            key: value for key, value in
            sorted(hotels_data.items(), key=lambda hotel_id: hotel_id[1]['price'], reverse=False)}
            # Обнуляем созданный ранее словарь и добавляем туда только те отели, которые соответствуют диапазону.
    elif command == '/bestdeal':
        hotels_data = {}
        for num, hotel in enumerate(data['data']['hotels'], 1):
            if min_rate < hotel['property']['reviewScore'] < max_rate and num <= count:
                hotels_data[hotel['property']['name']] = {
                    'name': hotel['property']['name'],
                    'id': hotel['hotel_id'],
                    'rating': hotel['property']['reviewScore'],
                    'price': round(hotel['property']['priceBreakdown']['grossPrice']['value']),
                    'photo': hotel['property']['photoUrls']}
    return hotels_data


