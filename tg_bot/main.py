from tg_bot.loader import bot
from telebot import custom_filters, logger
from handlers.search_handlers.filter import add_filters
from tg_bot.handlers.search_handlers import history
from tg_bot.api import search_hotel
from handlers.states_handler import survey_user

if __name__ == "__main__":
    add_filters(bot)
    logger.info('Бот запущен!')
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()