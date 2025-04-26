import requests
from tg_bot.config_data.config import headers

def request(method: str, url: str, query_string: dict) -> requests.Response:
    if method == "GET":
        response_get = requests.request("GET", url, params=query_string, headers=headers)
        return response_get
    elif method == "POST":
        response_post = requests.request("POST", url, json=query_string, headers=headers)
        return response_post