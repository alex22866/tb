import telebot
from telebot import types
bot = telebot.TeleBot('5731818519:AAHbKuoHDPUTXe4cfpQF9NJpF48TEB45nWk')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'привет':
#         bot.send_message(message.chat.id, 'и тебе привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == "photo":
#         photo = open('kotik.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'я тебя не понимаю', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def ger_user_photo(message):
    bot.send_message(message.chat.id, 'вау крутое фото')


@bot.message_handler(commands=['website'])
def website(message):
    #кнопки в команде
    markup = types.InlineKeyboardMarkup() #кнопка в команде
    markup.add(types.InlineKeyboardButton("жмяк", url="https://pypi.org/project/pip/")) #кнопка снизу
    bot.send_message(message.chat.id, 'посетить сайт', reply_markup=markup)#кнопка сверху


@bot.message_handler(commands=['help'])
def website(message):
    #кнопки в команде
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) #кнопка на панели
    website = types.KeyboardButton('вебсайт') #отдельная кнопка на панели
    a = types.KeyboardButton('start') #отдельная кнопка на панели
    b = types.KeyboardButton('start') #отдельная кнопка на панели
    c = types.KeyboardButton('start') #отдельная кнопка на панели
    start = types.KeyboardButton('start') #отдельная кнопка на панели


    markup.add(website, start, a, b, c) #кнопки на панели
    bot.send_message(message.chat.id, 'посетить сайт', reply_markup=markup)#кнопка сверху



bot.polling(none_stop=True)  # работает всегда
