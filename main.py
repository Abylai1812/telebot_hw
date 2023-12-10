import telebot
from env import BOT_TOKEN
from telebot import types

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_dog = types.KeyboardButton("/dog")
    item_github = types.KeyboardButton("github")
    item_balance = types.KeyboardButton("balance")
    markup.add(item_dog, item_github, item_balance)
    bot.send_message(message.chat.id, "Привет! Я бот. Выбери команду:", reply_markup=markup)

@bot.message_handler(commands=['dog'])
def send_dog(message):
    response = 'https://img.freepik.com/free-photo/isolated-happy-smiling-dog-white-background-portrait-4_1562-693.jpg?size=626&ext=jpg&ga=GA1.1.386372595.1697500800&semt=ais'
    bot.send_photo(message.chat.id, response)

@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    if message.text == 'github':
        bot.send_message(message.chat.id, "https://github.com/")
    elif message.text == 'balance':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item_withdraw = types.InlineKeyboardButton("Вывод", callback_data='withdraw')
        item_deposit = types.InlineKeyboardButton("Пополнить", callback_data='deposit')
        markup.add(item_withdraw, item_deposit)
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'withdraw':
        bot.send_message(call.message.chat.id, "Вы выбрали 'вывод'")
    elif call.data == 'deposit':
        bot.send_message(call.message.chat.id, "Вы выбрали 'пополнить'")

bot.polling()
