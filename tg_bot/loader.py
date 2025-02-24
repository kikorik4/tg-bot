from idlelib.history import History

from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from tg_bot.config_data import config
from tg_bot.database.user_history_db import UserDb

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db_user = UserDb('user.db')