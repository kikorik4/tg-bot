import os
from dotenv import find_dotenv

from flask.cli import load_dotenv

if not find_dotenv():
    exit('Переменные окружения не найдены, т.к. отсутсвует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку')
)