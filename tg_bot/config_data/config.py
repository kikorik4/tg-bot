import os
from dotenv import find_dotenv, load_dotenv


if not find_dotenv():
    exit('Переменные окружения не найдены, т.к. отсутсвует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', 'Поиск бюджетных отелей'),
    ('highprice', 'Поиск лучших отелей'),
    ('bestdeal', 'Настройка поиска'),
    ('history', 'История поиска')
)

url_city = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
url_hotel = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"