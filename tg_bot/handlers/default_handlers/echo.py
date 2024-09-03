from telebot.types import Message
from tg_bot.loader import bot

@bot.message_handler(state=None)
def echo_all(message):
    bot.reply_to(message, f'{message.text}')

