from tg_bot.loader import bot
from telebot import types
from logger import logger
from telebot.types import Message, Dict


def show_buttons_photo_need_yes_no(message: Message) -> None:
    """
    Вызов в чат инлайн-кнопок с вопросом - нужны ли пользователю фотографии?
    :rtype: object
    : param message : Message
    : return : None
    """
    logger.info(f'Вывод кнопок о необходимости фотографий пользователю. User_id: {message.chat.id}')
    keyboard_yes_no = types.InlineKeyboardMarkup()
    keyboard_yes_no.add(types.InlineKeyboardButton(text='ДА', callback_data='yes'))
    keyboard_yes_no.add(types.InlineKeyboardButton(text='НЕТ', callback_data='no'))
    bot.send_message(message.chat.id, "Нужно вывести фотографии?", reply_markup=keyboard_yes_no)

