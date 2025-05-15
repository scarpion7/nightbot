import telebot

TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Bu 'Tungi Hamroh' botidir.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yubordingiz: {message.text}")

bot.infinity_polling()
