import telebot
bot = telebot.TeleBot("7290518949:AAEpGjAlInIAayATTM1QFZgmZ5kVrP_U8tQ")
#функція, яка відповідає на будь-яке повідомлення таким самим
@bot.message_handler(func=lambda message: True)
def echo_message(message):
        bot.reply_to(message, message.text)
bot.polling()