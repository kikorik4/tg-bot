
import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY, url_hotel

headers_city = {
    "x-rapidapi-key": "06cd8b1e2dmsh19e47e3ff7423d3p1bca2ajsn6cedaafba959",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

headers_hotels = {
	"x-rapidapi-key": "06cd8b1e2dmsh19e47e3ff7423d3p1bca2ajsn6cedaafba959",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}


def get_city_id(city: str, ):
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers_city, params=querystring)
    return response



def get_hotel_id(dest_id: str, search_type: str, checkinDate: str, checkoutDate: str):
    querystring = {"dest_id": dest_id, "search_type": search_type, "arrival_date": checkinDate, "departure_date": checkoutDate, }
    response_hotels = requests.get(url_hotel, headers=headers_hotels, params=querystring)
    return response_hotels

try:
    def send_hotel_result(info,func):
        dest_id = info['data'][0]['dest_id']
        search_type = info['data'][0]['search_type']
        hotel_list = []
        hotels = func(f'{dest_id}', f'{search_type}', "2024-09-25", "2024-09-27")
        info_hotels = hotels.json()
        for i in info_hotels["data"]['hotels']:
           hotel_list.append(i['property']['name'])
        hotel_str = '\n'.join(hotel_list)
        return hotel_str
finally:
    pass


