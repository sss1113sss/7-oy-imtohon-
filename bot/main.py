import telebot
import time
import requests
from dotenv import load_dotenv
import os
import django
from telebot import types

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automobiles.settings')
django.setup()

from bot.models import WeatherInfo
load_dotenv()

load_dotenv()

BOT_TOKEN = os.environ.get('6758743739:AAFdD0cIKmWF8kulYs--Wfa0k6SdBnoLwzk')
WEATHER_API = os.environ.get('6f89d8dda0daea2d92b16c516adf1ac0')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, "Bizning ilk botimizga hush kelibsiz!!..")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    weather = WeatherInfo.objects.all()
    weather_info = "\n".join([f"{weather.email} ---> {weather.temperature} {weather.received_at}" for weather in weather])
    bot.send_message(message.chat.id, f"Weather Information:\n{weather}")

    holatuz = {"Clouds":"🌥️","Clear":" musoffo osmon ", "Sunny":"quyoshli"}
    city = message.text[9:]
    data = get_full_data(city)
    # print(str(data))
    holat = data.get("weather", [])[0].get("main", "xatolik")
    a = None
    try:
        a = holatuz[holat]
    except:
        a = "bilmiman qanaqa holatda ekanini"
    temp = round(data.get("main", {}).get('temp', 0) - 273.15)
    bot.send_message(message.chat.id, f"hozirda {city}da havo {temp} bo'lishi kutulmoqda!..\nhavo holati {a}")




def get_full_data(city):
    url = WEATHER_API + city
    response = requests.get(url)
    return response.json()



bot.infinity_polling()

