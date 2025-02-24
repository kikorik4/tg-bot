import sqlite3
from logger import logger

class UserDb:
    def __init__(self, db_user):
        self.connection = sqlite3.connect(db_user, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.set_up_db()

    def set_up_db(self):
        logger.info('Я создаю базу)))')
        with self.connection:
            return self.cursor.execute('''CREATE TABLE IF NOT EXISTS User(
            userId INTEGER PRIMARY KEY ,
            firstname TEXT,
            lastname TEXT,
            AGE INT NOT NULL DEFAULT 1)
            ''')

    def check_user(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT `userId` FROM User WHERE `userId` = ?')
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO User(UserId) VALUES (?)', (user_id))


    def filling_db(self, data):
        with self.connection:
            self.cursor.execute('UPDATE User SET firstname=?, lastname=?, AGE=? WHERE userId=?', (data['name'], data['surname'], data['age'], data['id']))