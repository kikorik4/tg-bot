from loader import bot
import handlers
import sqlite3

name = None

@bot.message_handler(commands=['/start'])
def start(message):
    connection = sqlite3.connect('user_db.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users '
                   '(id int auto_increment primary_key, '
                   'name varchar(50), pass varchar(50))' )
    connection.commit()
    cursor.close()
    connection.close()
    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите твое имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, f'Привет, {name}')

    connection = sqlite3.connect('user_db.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users name VALUES '%s'") % name
    connection.commit()
    cursor.close()
    connection.close()


    bot.send_message(message.chat.id, 'Пользователь зарегесрирован! Список всех пользователеей:')
    bot.register_next_step_handler(message, user_list)

def user_list():
    connection = sqlite3.connect('user_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    info = ''
    for i_user in users:
      info += f'Имя: {i_user[1]}'

    cursor.close()
    connection.close()



if __name__ == "__main__":
    bot.infinity_polling()