import sqlite3
import json


class UserHistoryDb:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.set_up_table()

    def set_up_table(self):
        with self.connection:
            return self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS UserHistory(
            userID INT,
            search_date datetime DEFAULT CURRENT_DATE,
            command TEXT,
            data json)
            ''')

    def set_data(self, user_id: int, command: str, data: dict) ->sqlite3.connect('history_user_db').cursor():
        with self.connection:
            return self.cursor.execute('''
            INSERT INTO UserHistory(`userID`, `command`, `data`)
            VALUES (?,?,?)''', (user_id, command, json.dumps(data)))

    def get_data(self, user_id: int, count: int) -> sqlite3.connect('history_user_db'):
        with self.connection:
            return self.cursor.execute('''
            SELECT `search_data`, `command`, `data` FROM UserHistoty
            WHERE `userID` = ? LIMIT?''', (user_id, count))

    def del_data(self, user_id: int) -> sqlite3.connect('history_user_db'):
        with self.connection:
            return self.cursor.execute('''
            DELETE FROM WHERE `userID` = ?''', (user_id,))

