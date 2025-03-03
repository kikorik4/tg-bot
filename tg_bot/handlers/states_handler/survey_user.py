from venv import logger
from tg_bot.states.survey_user_states import MyStates
from tg_bot.loader import bot, db_user


@bot.message_handler(commands=['survey'])
def start_survey(message):
    if not db_user.check_user(message.from_user.id):
        db_user.add_user(message.from_user.id)
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['id'] = message.from_user.id
    bot.send_message(message.chat.id, 'Привет! Напиши свое имя')


@bot.message_handler(state=MyStates.name)
def save_name(message):
    bot.send_message(message.chat.id, 'Напиши свою фамилию')
    bot.set_state(message.from_user.id, MyStates.surname, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
        logger.info('Я записываю имя')


@bot.message_handler(state=MyStates.surname)
def ask_age(message):
    bot.send_message(message.chat.id, 'Сколько тебе лет?')
    bot.set_state(message.from_user.id, MyStates.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['surname'] = message.text

def is_digit(message):
    return message.text.isdigit()


@bot.message_handler(state=MyStates.age, is_digit=True)
def answer_report(message):
        logger.info('Я туутаа')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['age'] = int(message.text)
            bot.send_message(message.chat.id, f"Введеная информация:\nИмя: {data['name']}\nФамилия: {data['surname']}\nВозраст: {data['age']}")
            db_user.filling_db(data)
            bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.age, is_digit=False)
def age_incorrect(message):
    logger.error('Не тот формат возраста')
    bot.send_message(message.chat.id, 'Ты неправильно ввел возраст!')

