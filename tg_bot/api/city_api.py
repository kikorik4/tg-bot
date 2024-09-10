
import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY, url_hotel

headers_city = {
    "x-rapidapi-key": "c4daf61859mshf367daf96a89533p1fa519jsn407321d2c2ff",
    "x-rapidapi-host": "booking-com18.p.rapidapi.com"
}

headers_hotels = {
    "x-rapidapi-key": "c4daf61859mshf367daf96a89533p1fa519jsn407321d2c2ff",
    "x-rapidapi-host": "booking-com18.p.rapidapi.com"
}


def get_city_id(city: str, ):
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers_city, params=querystring)
    return response


trying = get_city_id('London')
info_city = trying.json()
print(json.dumps(info_city, indent=4, sort_keys=True))



def get_hotel_id(city_id: str, checkinDate: str, checkoutDate):
    querystring = {"locationId": city_id, "checkinDate": checkinDate, "checkoutDate": checkoutDate, "units": "metric", "temperature": "c"}
    response_hotels = requests.get(url_hotel, headers=headers_hotels, params=querystring)
    return response_hotels

def unpackjson(key, data):
    '''Функция находит нужное значение по ключу.'''
    try:
        result = {key: data[key]}
        return result
    except KeyError:
        for element in data:
            if type(data[element]) is dict:
                if data[element][key]:
                    return {key: data[element][key]}
                else:
                    unpackjson(key, data[element])


id_cities = unpackjson('data'[1]['id'], info_city)
hotels = get_hotel_id(info_city.get('id'), '2024-09-10', '2024-09-11')
