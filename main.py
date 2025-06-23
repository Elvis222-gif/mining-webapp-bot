import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "YOUR_BOT_TOKEN"
WEBAPP_URL = "https://your-webapp-url.onrender.com"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton("🚀 Start Mining", web_app=WebAppInfo(url=WEBAPP_URL))
    markup.add(webapp_button)
    bot.send_message(message.chat.id, "👋 Welcome to PEPE Mining!", reply_markup=markup)

bot.infinity_polling()