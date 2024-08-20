import telebot
from telebot import types
from parsing import *


TOKEN = '7128738421:AAGMSxZkvKmTBwSMj79c-jJneundgWg9UO4'
bot = telebot.TeleBot(TOKEN)
choice = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Description', callback_data='desctiption')
btn2 = types.InlineKeyboardButton('Photo', callback_data='photo')
btn3 = types.InlineKeyboardButton('Quit', callback_data='quit')
choice.add(btn1, btn2, btn3)
num_of_new = 0


@bot.message_handler(commands=['start'])
def start(message):
    chat = message.chat.id
    bot.send_message(chat, 'Привет, я новостной бот!')


@bot.message_handler(content_types=['text'])
def list_mews(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, get_list_news())
    msg = bot.send_message(chat_id, 'Выбери номер новости: ')
    bot.register_next_step_handler(msg, new)

def new(c):
    global num_of_new
    chat_id = c.chat.id
    num_of_new = int(c.text)
    bot.send_message(chat_id, 'Выберите фото или описание какой-либо новости: ', reply_markup=choice)

@bot.callback_query_handler(func=lambda c: True)
def get_description_or_photo(c):
    chat_id = c.message.chat.id
    if c.data == 'desctiption':
        bot.send_message(chat_id, get_one_new(num_of_new))
    elif c.data == 'photo':
        bot.send_message(chat_id, get_photo(num_of_new))
    elif c.data == 'quit':
        bot.send_message(chat_id, 'До свидания')

bot.polling()