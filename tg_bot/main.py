from tg_bot.loader import bot
from tg_bot.config_data.config import RAPID_API_KEY
from tg_bot.handlers.search_handlers.search_hotel import start,get_checkIn,get_checkOut
from tg_bot.api.city_api import get_city_id, get_hotel_id



if __name__ == "__main__":
    bot.infinity_polling()
