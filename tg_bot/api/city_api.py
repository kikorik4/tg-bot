
import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY, url_hotel

headers_city = {
	"x-rapidapi-key": "045c1f4e08msh5d745e6d7391549p195bccjsncf8849b837e3",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

headers_hotels = {
	"x-rapidapi-key": "045c1f4e08msh5d745e6d7391549p195bccjsncf8849b837e3",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}


def get_city_id(city: str, ):
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers_city, params=querystring)
    return response


trying = get_city_id('London')
info_city = trying.json()
print(json.dumps(info_city, indent=4))




def get_hotel_id(dest_id: str, search_type: str, checkinDate: str, checkoutDate):
    querystring = {"dest_id": dest_id, "search_type": search_type, "arrival_date": checkinDate, "departure_date": checkoutDate, }
    response_hotels = requests.get(url_hotel, headers=headers_hotels, params=querystring)
    return response_hotels

dest_id = info_city['data'][0]['dest_id']
search_type = info_city['data'][0]['search_type']
print(dest_id)
hotels = get_hotel_id(f'{dest_id}', f'{search_type}',"2024-09-20", "2024-09-21" )
info_hotels = hotels.json()
print(json.dumps(info_hotels, indent=4))