import sqlite3


class UserDb:
    def __init__(self, db_user):
        self.connection = sqlite3.connect(db_user, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.set_up_db()

    def set_up_db(self):
        """
                :return: Создание базы данных
                """
        with self.connection:
            return self.cursor.execute('''CREATE TABLE IF NOT EXISTS User(
            userId INTEGER PRIMARY KEY ,
            firstname TEXT,
            lastname TEXT,
            AGE INT NOT NULL DEFAULT 1)
            ''')

    def check_user(self, user_id):
        """
                :param user_id: идентификатор пользователя
                :return: Наличие/отсутствие пользователя
                """
        with self.connection:
            result = self.cursor.execute('SELECT `userId` FROM User WHERE `userId` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        """
                :param user_id: Идентификатор пользователя
                :return: Добавить пользователя  БД
                """
        with self.connection:
            return self.cursor.execute('INSERT INTO User(UserId) VALUES (?)', (user_id,))

    def filling_db(self, data):
        """
                Функция записи информации о пользователе из словаря.
                :param data: Dict информация о пользователе
                :return:
                """
        with self.connection:
            self.cursor.execute('UPDATE User SET firstname=?, lastname=?, AGE=? WHERE userId=?',
                                (data['name'], data['surname'], data['age'], data['id']))
