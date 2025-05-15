import telebot

from flask import Flask
import threading
import telebot
import os

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Oddiy Flask route (health check uchun)
@app.route('/')
def index():
    return "Bot is running."

# Botni alohida threadda ishga tushirish
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Botni background threadda ishga tushuramiz
    threading.Thread(target=run_bot).start()

    # Flask serverni ishga tushuramiz, Render portidan foydalanamiz
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


TOKEN = '7025127609:AAHaAtdtx_Ip3Q7uB3AXSCmM_uPw8Ugc1zU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Bu 'Tungi Hamroh' botidir.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yubordingiz: {message.text}")

bot.infinity_polling()
