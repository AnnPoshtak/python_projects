import telebot
import time
user_id = ""
m = ""
text = ""
key = "7684005774:AAHlTf1S47ThB33kPBypJdUQhTliTekYSsA"
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Я бот спамер😈. Ти можеш тегнути людину і буде n повідомлень підряд з закликанням цієЇ людину. Напиши команду /settings, щоб налаштувати і почати спам")
@bot.message_handler(commands=["settings"])
def settings(message):
    global user_id
    global m
    bot.send_message(message.chat.id,"Вкажіть нік людини (@...). Якщо нік не треба, введіть '-'")
    bot.register_next_step_handler(message, saveUserId)

def saveUserId(message):
    global user_id
    user_id = message.text
    if user_id == "-":
        user_id = "Немає"
    bot.send_message(message.chat.id, f"Нік збережено: {user_id}\nСкільки повідомлень потрібно надіслати?")
    bot.register_next_step_handler(message, save_count)

def save_count(message):
    global m
    m = message.text
    bot.send_message(message.chat.id, f"Кільксть повідомлень:{m}.\nВведіть текст повідомлення. Або '-'")
    bot.register_next_step_handler(message, save_message)

def save_message(message):
    global text
    text = message.text
    if text == "-":
        text = "Немає"
    bot.send_message(message.chat.id,f"Готово! Нік: {user_id}\nКільксть повідомлень: {m}\nПовідомлення: {text}.\n Щоб почати спам, напишіть /start_spam")

@bot.message_handler(commands=["start_spam"])
def start_spam(message):
    global user_id, m, text
    if user_id == "Немає" and text == "Немає":
        for i in range(int(m)):
            bot.send_message(message.chat.id,"Хей, людина!")
            time.sleep(0.5)
    elif user_id != "Немає" and text == "Немає":
        for i in range(int(m)):
            bot.send_message(message.chat.id, f"Хей, {user_id}!")
            time.sleep(0.5)
    elif user_id == "Немає" and text != "Немає":
        for i in range(int(m)):
            bot.send_message(message.chat.id, text)
            time.sleep(0.5)
    else:
        for i in range(int(m)):
            bot.send_message(message.chat.id, f"{user_id}!, {text}")
            time.sleep(0.5)
bot.infinity_polling()