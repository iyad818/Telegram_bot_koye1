import telebot

# إضافة التوكن مباشرة داخل الكود
Token = "7931337756:AAFpgGzj0mxsxN8iRjj7bqBRBRN2tZsmbQY"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا بك! هذا البوت يعمل على استضافة Koyeb 🚀")

bot.polling()
