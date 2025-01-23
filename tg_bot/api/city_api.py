import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY, url_hotel
#from tg_bot.blahblah import id

headers = headers = {
 "x-rapidapi-key": "c4daf61859mshf367daf96a89533p1fa519jsn407321d2c2ff",
 "x-rapidapi-host": "booking-com15.p.rapidapi.com"
}


def get_city_id(city: str, ):
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers, params=querystring)
    return response

def get_api_city(city: str):
    return f''



def get_hotel_id(dest_id: str, search_type: str, checkinDate: str, checkoutDate: str):
    querystring = {"dest_id": dest_id, "search_type": search_type, "arrival_date": checkinDate, "departure_date": checkoutDate, }
    response_hotels = requests.get(url_hotel, headers=headers, params=querystring)
    return response_hotels

def send_hotel_result(info, checkIn, checkOut, func):
    dest_id = info['data'][0]['dest_id']
    search_type = info['data'][0]['search_type']
    hotel_list = []
    hotels = func(f'{dest_id}', f'{search_type}', f'{checkIn}', f"{checkOut}")
    info_hotels = hotels.json()
    #for i in info_hotels['data']['filters'][6]['options']:
       # hotel_list.append(i['title'])
   # hotel_str = '\n'.join(hotel_list)
    return info_hotels

#def get_api_data(info, func):
#    return f'{id}'






