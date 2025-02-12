from tg_bot.loader import bot
from telebot import custom_filters
from tg_bot.config_data.config import RAPID_API_KEY
from tg_bot.handlers.search_handlers.search_hotel import start
from tg_bot.api.city_api import get_city_id, get_hotel_id



if __name__ == "__main__":
    print('Бот запущен!')
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()