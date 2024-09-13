from loader import bot
import handlers
from config_data.config import RAPID_API_KEY



if __name__ == "__main__":
    bot.infinity_polling()

import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"

querystring = {"query":"Prague"}

headers = {
	"x-rapidapi-key": "8dd46fee20msh76d7db83c926e3dp17885cjsne81d88aa8a5c",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())





import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getFilter"

querystring = {"dest_id":"-2092174","search_type":"CITY","arrival_date":"2024-09-14","departure_date":"2024-09-15"}

headers = {
	"x-rapidapi-key": "8dd46fee20msh76d7db83c926e3dp17885cjsne81d88aa8a5c",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())