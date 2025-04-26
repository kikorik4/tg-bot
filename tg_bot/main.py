from tg_bot.loader import bot
from telebot import custom_filters, logger
from handlers.search_handlers.filter import add_filters
import handlers
from handlers.default_handlers import start
from utils.set_bot_commands import set_default_command
from handlers.search_handlers import commands
from keyboards.inline import delete_history, inline_calendar, all_buttons
from handlers.callback_handler import photo_need, check_date

if __name__ == "__main__":
    add_filters(bot)
    logger.info('Бот запущен!')
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()