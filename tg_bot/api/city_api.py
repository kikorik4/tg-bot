import requests
import json
from pprint import pprint
from tg_bot.config_data.config import url_city, RAPID_API_KEY


headers = {
	"x-rapidapi-key": "35b230ac1bmsh5b267bb37a0e7f4p107a32jsn451e1598ff0c",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

def get_city_id(city: str, ) :
    querystring = {"query": city}
    response = requests.request("GET", url_city, headers=headers, params=querystring)
    return response

trying = get_city_id('Moscow')
print(trying.json())
