import telebot
from telebot import SimpleCustomFilter


class IsDigitNoMany(SimpleCustomFilter):
    key = 'count_digit'

    def check(self, message):
        return 0 < int(message.text.strip()) <= 10

def add_filters(bot):
    bot.add_custom_filter(IsDigitNoMany())
    bot.add_custom_filter(telebot.custom_filters.IsDigitFilter())


