import telebot
from decouple import config


try:
    token = config('TOKEN')
    bot = telebot.TeleBot(token)
except:
    bot = telebot.TeleBot('Error. Token is incorrect.')
