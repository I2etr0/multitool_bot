import token
import currency_parser
import telebot
from telebot import types

TOKEN = '5417008537:AAFJinudA_4-BrwFv0xaVlpXWXPS6DDBUYI'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = types.KeyboardButton('Доллар')
    eur = types.KeyboardButton('Евро')
    gel = types.KeyboardButton('Грузинский Лари')
    markup.add(usd, eur, gel)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

    # elif message.text == 'Доллар':
    #     bot.send_message(message.chat.id,
    #                      f"{message.text}: " + str(currency_parser.r[0][-7:] + f' на {currency_parser.date[-13:]}'))
    #
    # elif message.text == 'Евро':
    #     bot.send_message(message.chat.id,
    #                      f"{message.text}: " + str(currency_parser.r[1][-7:] + f' на {currency_parser.date[-13:]}'))
    #
    # elif message.text == 'Грузинский Лари':
    #     bot.send_message(message.chat.id,
    #                      f"{message.text}: " + str(currency_parser.r[66][-7:] + f' на {currency_parser.date[-13:]}'))

    if message.text == 'Доллар':
        bot.send_message(message.chat.id, f"{message.text}: ")

    elif message.text == 'Евро':
        bot.send_message(message.chat.id, f"{message.text}: ")

    elif message.text == 'Грузинский Лари':
        bot.send_message(message.chat.id, f"{message.text}: ")


bot.polling(none_stop=True)
