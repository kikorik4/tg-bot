import sqlite3


class UserHistoryDb:
    """
        Пользовательский класс базу данных для работы с пользователем и его историей поиска
        """

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.set_up_table()

    def set_up_table(self):
        """
               Устанавливает таблицу в БД если их нет
               :return:
               """
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS UserHistory(
            userID INT,
            search_date datetime DEFAULT CURRENT_DATE,
            command TEXT,
            input_city TEXT,
            destination_id TEXT,
            photo_need TEXT)
            ''')

    def set_data(self, user_id: int, data: dict) -> sqlite3.connect('history_user.db').cursor():
        """
                Запись в БД пользователя, введенной команды и словаря отелей
                :param user_id: идентификатор пользователя
                :param command: команда поиска отелей
                :param data: Словарь отелей
                :return:
                """
        with self.connection:
            return self.cursor.execute('''
            INSERT INTO UserHistory(`userID`, `command`, `input_city`, `destination_id`, `photo_need`)
            VALUES (?,?,?,?,?)''', (
            user_id, data["command"], data["input_city"], data['destination_id'], data["photo_need"]))

    def get_data(self, user_id: int, count: int) -> sqlite3.connect('history_user.db').cursor():
        """
                Достать из БД историю
                :param user_id:Идентификатор пользователя
                :param count:Количество отелей
                :return:
                """
        with self.connection:
            return self.cursor.execute('''
            SELECT `userID`, `command`, `input_city`, `destination_id`, `photo_need` FROM UserHistory
            WHERE `userID` = ? ORDER BY `search_date` ASC LIMIT ?''', (user_id, count))

    def del_data(self, user_id: int) -> sqlite3.connect('history_user.db'):
        """
                Стереть историю
                :param user_id: Идентификатор пользователя
                :return:
                """
        with self.connection:
            return self.cursor.execute('''
            DELETE FROM WHERE `userID` = ?''', (user_id,))
