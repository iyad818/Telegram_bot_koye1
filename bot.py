import telebot

# إضافة التوكن مباشرة داخل الكود
Token = "7596905170:AAHEIrzF4tsGWpcJN0QmR0rtFS3SoNy6h7Q"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا بك! هذا البوت يعمل على استضافة Koyeb 🚀\n مرحبا \n Goode")

bot.polling()
