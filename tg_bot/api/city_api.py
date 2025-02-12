import requests
import json
from logger import logger
from tg_bot.loader import bot
from tg_bot.config_data.config import url_city, url_hotel
#from tg_bot.blahblah import id


headers = {
 "x-rapidapi-key": "c4daf61859mshf367daf96a89533p1fa519jsn407321d2c2ff",
 "x-rapidapi-host": "booking-com15.p.rapidapi.com"
}


def get_city_id(city: str, ):
        querystring = {"query": city}
        response = requests.request("GET", url_city, headers=headers, params=querystring)
        if response:
            logger.info('response')
            city_json = response.json()
            dest_id = city_json['data'][0]['dest_id']
            if dest_id is str:
                return dest_id
           # else:
               # raise TypeError


def get_api_city(city: str):
    return f''



def get_hotel_id(dest_id: str, search_type: str, checkinDate: str, checkoutDate: str):
    querystring = {"dest_id": dest_id, "search_type": search_type, "arrival_date": checkinDate, "departure_date": checkoutDate, }
    try:
        response_hotels = requests.get(url_hotel, headers=headers, params=querystring)
        if response_hotels:
            logger.info('response')
            return response_hotels
        else:
            logger.error('По вашему запросу ничего не найдено. Попробуйте снова /start')
            return 'По вашему запросу ничего не найдено. Попробуйте снова /start'
    except BaseException as e:
        logger.exception(e)


def send_hotel_result(info, checkIn, checkOut, func):
    try:
        dest_id = info['data'][0]['dest_id']
        search_type = info['data'][0]['search_type']
        hotel_list = []
    except KeyError:
        logger.error('Something was wrong!')
    hotels = func(f'{dest_id}', f'{search_type}', f'{checkIn}', f"{checkOut}")
    info_hotels = hotels.json()
    for i in info_hotels['data']['filters'][4]['options']:
       hotel_list.append(i['title'])
    hotel_str = '\n'.join(hotel_list)
    return hotel_str

#def get_api_data(info, func):
#    return f'{id}'






