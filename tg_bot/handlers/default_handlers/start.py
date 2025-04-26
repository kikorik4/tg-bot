from tg_bot.loader import bot

@bot.message_handler(commands=['start'])
def bot_start(message) -> None:
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
