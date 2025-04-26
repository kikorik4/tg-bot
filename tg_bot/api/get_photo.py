from typing import Union

import requests
import json
from tg_bot.config_data.config import url_from_photo, headers


def get_photo_hotel(hotel_id: int, count_photo: str) -> Union[list, bool]:
    media = []
    querystring = {
        'hotel_id': hotel_id
    }
    response = requests.request("GET", url_from_photo, headers=headers, params=querystring)
    if response:
        data = json.loads(response.text)['hotelImages']
        if data:
            for photo in data:
                media.append(photo['baseUrl'].replace('{size}', 'b'))
                if len(media) >= int(count_photo):
                    break
            return media