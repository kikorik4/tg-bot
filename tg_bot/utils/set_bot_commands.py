from telebot.types import BotCommand
from tg_bot.config_data.config import DEFAULT_COMMANDS

def set_default_command(bot):
    bot.set_my_command(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )