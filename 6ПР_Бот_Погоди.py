import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = '7794907475:AAEQQJXSSNq_KAwdfLgGu9-X3Dly72QxnVI'
bot = telebot.TeleBot(TOKEN)

# Функція для отримання погоди з сайту для поточного дня або часу доби
def get_weather_data(day=None, time_of_day=None):
    url = 'https://sinoptik.ua/погода-луцьк'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if day is None and time_of_day is None:
        # Отримання даних для сьогоднішнього дня
        temperature = soup.find('p', class_='today-temp').text.strip()
        weather = soup.find('div', class_='description').text.strip()
        return f"Температура: {temperature}\nПогода: {weather}"

    if time_of_day:
        # Отримання температури для певного часу доби
        times_mapping = {
            'ніч': 0,
            'ранок': 1,
            'день': 2,
            'вечір': 3
        }
        forecast_row = soup.find('tr', class_='temperature')
        if forecast_row:
            temp_cells = forecast_row.find_all('td')
            if len(temp_cells) > times_mapping[time_of_day]:
                temp = temp_cells[times_mapping[time_of_day]].text.strip()
                return f"Температура на {time_of_day.capitalize()}: {temp}"
            else:
                return "Не вдалося знайти дані для обраного часу доби."
        else:
            return "Не вдалося знайти рядок з прогнозом."

    # Отримання температури і погоди для конкретного дня тижня
    days_block = soup.find_all('div', class_='main')
    days_mapping = {
        'понеділок': 0,
        'вівторок': 1,
        'середа': 2,
        'четвер': 3,
        'пʼятниця': 4,
        'субота': 5,
        'неділя': 6
    }

    index = days_mapping.get(day)
    if index is not None and index < len(days_block):
        day_block = days_block[index]
        temp_min = day_block.find('div', class_='temperature').find_all('span')[0].text.strip()
        temp_max = day_block.find('div', class_='temperature').find_all('span')[-1].text.strip()
        weather = day_block.find('div', class_='weatherIco').get('title')
        return f"Температура на {day.capitalize()}:\nМінімум: {temp_min}\nМаксимум: {temp_max}\nПогода: {weather}"
    else:
        return "Не вдалося знайти дані для обраного дня."

# Команда старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton("Температура і погода зараз")
    btn2 = types.KeyboardButton("Температура і погода на тиждень")
    btn3 = types.KeyboardButton("Температура відносно години")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=markup)

# Обробка натискання кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Температура і погода зараз":
        weather_info = get_weather_data()
        bot.send_message(message.chat.id, weather_info)

    elif message.text == "Температура і погода на тиждень":
        markup = types.InlineKeyboardMarkup()
        days = ["Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця", "Субота", "Неділя"]
        for day in days:
            markup.add(types.InlineKeyboardButton(day, callback_data=day.lower()))
        bot.send_message(message.chat.id, "Виберіть день:", reply_markup=markup)

    elif message.text == "Температура відносно години":
        markup = types.InlineKeyboardMarkup()
        times_of_day = ["ніч", "ранок", "день", "вечір"]
        for time in times_of_day:
            markup.add(types.InlineKeyboardButton(f"Температура на {time}", callback_data=f"time_{time}"))
        bot.send_message(message.chat.id, "Виберіть час доби:", reply_markup=markup)

# Обробка callback даних
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data in ["понеділок", "вівторок", "середа", "четвер", "пʼятниця", "субота", "неділя"]:
        weather_info = get_weather_data(day=call.data)
        bot.send_message(call.message.chat.id, weather_info)

    elif call.data.startswith("time_"):
        time_of_day = call.data.split("_")[1]
        weather_info = get_weather_data(time_of_day=time_of_day)
        bot.send_message(call.message.chat.id, weather_info)

# Запуск бота
bot.polling(none_stop=True)