from tg_bot.loader import bot

@bot.message_handler(state="*", commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "Твои этапы отменены.")
    bot.delete_state(message.from_user.id, message.chat.id)