# import password
import currency_parser
import weather_parser
import telebot
from telebot import types

TOKEN = password.token
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency = types.KeyboardButton('Курс валют')
    link = types.KeyboardButton('Погода')
    markup.add(currency, link)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types='text')
def menu(message):
    if message.text == 'Курс валют':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        usd = types.KeyboardButton('Доллар')
        eur = types.KeyboardButton('Евро')
        gel = types.KeyboardButton('Грузинский Лари')
        back = types.KeyboardButton('Назад')
        markup.add(usd, eur, gel, back)

        bot.send_message(message.chat.id, 'Выбери валюту:'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Погода':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today = types.KeyboardButton('Сегодня')
        tomorrow = types.KeyboardButton('Завтра')
        tomorrow_x2 = types.KeyboardButton('Послезавтра')
        back = types.KeyboardButton('Назад')
        markup.add(today, tomorrow, tomorrow_x2, back)

        bot.send_message(message.chat.id, 'Выбери день:'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Сегодня':
        bot.send_message(message.chat.id, f"{message.text}:\n" + str(weather_parser.Today.today.r[0][0:80]))

    elif message.text == 'Завтра':
        bot.send_message(message.chat.id, f"{message.text}:\n" + str(weather_parser.Other_days.other.r[1][0:80]))

    elif message.text == 'Послезавтра':
        bot.send_message(message.chat.id, f"{message.text}:\n" + str(weather_parser.Other_days.other.r[2][0:80]))

    elif message.text == 'Доллар':
        bot.send_message(message.chat.id, f"{message.text}: " + str(currency_parser.r[0][-7:] + f' на {currency_parser.date[-13:]}'))

    elif message.text == 'Евро':
        bot.send_message(message.chat.id, f"{message.text}: " + str(currency_parser.r[1][-7:] + f' на {currency_parser.date[-13:]}'))

    elif message.text == 'Грузинский Лари':
        bot.send_message(message.chat.id, f"{message.text}: " + str(currency_parser.r[66][-7:] + f' на {currency_parser.date[-13:]}'))

    elif message.text == 'Назад':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        currency = types.KeyboardButton('Курс валют')
        link = types.KeyboardButton('Погода')
        markup.add(currency, link)

        bot.send_message(message.chat.id, 'Чем могу помочь?'.format(message.from_user), reply_markup=markup)



bot.polling(none_stop=True)
