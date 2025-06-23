import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8081295066:AAHUdMNTd4MdZDMSAK5c3w94UZsQGXQ6Vlg"
WEBAPP_URL = "https://pepe-miner.onrender.com"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton("🚀 Start Mining", web_app=WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_button)
    bot.send_message(message.chat.id, "👋 Welcome to PEPE Mining!\n\nTap below to start mining real PEPE tokens inside our WebApp. 💰⛏️", reply_markup=markup)

bot.infinity_polling()
