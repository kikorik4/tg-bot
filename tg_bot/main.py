from loader import bot
from config_data.config import RAPID_API_KEY
from handlers.search_handlers.search_hotel import start, get_city


if __name__ == "__main__":
    bot.infinity_polling()
