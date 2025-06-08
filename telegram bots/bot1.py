import telebot
import time
token = "7686193087:AAF0I_iMMaT-XgMleJPSOXcK1qXl1XLzv20"
bot = telebot.TeleBot(token)
mess = ["спам",":)","мене не зупинити","unstopuble","the best bot"]
@bot.message_handler(content_types=['text'])
def start(message):
    for i in range(5):
        bot.send_message(message.chat.id, mess[i])
        time.sleep(1)

bot.infinity_polling()