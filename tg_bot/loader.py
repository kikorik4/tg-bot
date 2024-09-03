from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(Token=config.BOT_TOKEN, state_storage=storage)