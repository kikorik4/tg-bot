
import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY, url_hotel

headers_city = {
	"x-rapidapi-key": "8dd46fee20msh76d7db83c926e3dp17885cjsne81d88aa8a5c",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

headers_hotels = {
	"x-rapidapi-key": "8dd46fee20msh76d7db83c926e3dp17885cjsne81d88aa8a5c",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}


def get_city_id(city: str, ):
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers_city, params=querystring)
    return response


trying = get_city_id('London')
info_city = trying.json()




def get_hotel_id(dest_id: str, checkinDate: str, checkoutDate):
    querystring = {"dest_id": dest_id, "search_type":"CITY", "arrival_date": checkinDate, "departure_date": checkoutDate, }
    response_hotels = requests.get(url_hotel, headers=headers_hotels, params=querystring)
    return response_hotels

dest_id = info_city['data'][0]['dest_id']
hotels = get_hotel_id(f'{dest_id}',"2024-09-14", "2024-09-15" )
info_hotels = hotels.json()
result = json.loads(info_hotels)
print(json.dumps(result, indent=4))