import parser
import telebot
from telebot import types

TOKEN = "5417008537:AAFJinudA_4-BrwFv0xaVlpXWXPS6DDBUYI"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency = types.KeyboardButton('Курс валют')
    link = types.KeyboardButton('Сократить ссылку')
    markup.add(currency, link)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types='text')
def menu(message):
    if message.text == 'Курс валют':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        usd = types.KeyboardButton('Доллар')
        eur = types.KeyboardButton('Евро')
        gel = types.KeyboardButton('Грузинский Лари')
        # usd = types.KeyboardButton('Имя_кнопки')
        markup.add(usd, eur, gel)

        bot.send_message(message.chat.id, 'Выбери валюту:'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Сократить ссылку':
        pass

    elif message.text == 'Доллар':
        bot.send_message(message.chat.id, f"{message.text}: " + str(parser.r[0][-7:] + f' на {parser.date[-13:]}'))

    elif message.text == 'Евро':
        bot.send_message(message.chat.id, f"{message.text}: " + str(parser.r[1][-7:] + f' на {parser.date[-13:]}'))

    elif message.text == 'Грузинский Лари':
        bot.send_message(message.chat.id, f"{message.text}: " + str(parser.r[66][-7:] + f' на {parser.date[-13:]}'))


bot.polling(none_stop=True)