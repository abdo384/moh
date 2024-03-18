

import telebot

# تعريف التوكن الخاص بالبوت الخاص بك
TOKEN = '6363420983:AAGb4yIDwpU112WijmfYKB5M2EBr2UzLmJs'

# إنشاء كائن البوت
bot = telebot.TeleBot(TOKEN)

# استجابة للرسائل التي تحتوي على "/start" أو "/help"
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك! أنا بوت الردود المتطور. أرسل لي رسالة وسأرد عليك.")

# استجابة مخصصة لنوع معين من الرسائل
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'مرحبا' in message.text:
        bot.reply_to(message, "مرحبًا! كيف يمكنني مساعدتك؟")
    elif 'كيف حالك' in message.text:
        bot.reply_to(message, "أنا بخير، شكرًا لسؤالك!")
    else:
        bot.reply_to(message, "عذرًا، لم أفهم ما قصدت.")

# تشغيل البوت
bot.polling()
