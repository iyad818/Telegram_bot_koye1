import telebot
import os

TOKEN = os.getenv("7931337756:AAFpgGzj0mxsxN8iRjj7bqBRBRN2tZsmbQY")  # قراءة التوكن من المتغيرات البيئية
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحبا بك! هذا البوت يعمل على استضافة Koyeb 🎉 نحن نصفق لـ Koyeb 🌹")

print("✅ البوت يعمل...")
bot.infinity_polling()
