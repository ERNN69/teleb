import telebot
from time import sleep

TOKEN = '7104068355:AAGwQqs9xbNFHFuI1nkNKBNxSnGAie_eIvA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, че надо?')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет')

    elif message.text == "как дела":
        sleep(2)
        bot.send_message(message.from_user.id, 'Норм')
    elif message.text == "что делаешь?":
        sleep(2)
        bot.send_message(message.from_user.id, 'спать иду')
    elif message.text == "что делаешь?":
        sleep(2)
        bot.send_message(message.from_user.id, 'хз')
    elif message.text == "рост?":
        sleep(2)
        bot.send_message(message.from_user.id, '178cm')
    elif message.text == "как зовут?":
        sleep(2)
        bot.send_message(message.from_user.id, 'ERA')
    elif message.text == "ты yел?":
        sleep(2)
        bot.send_message(message.from_user.id, 'да')
    elif message.text == "пока":
        sleep(2)
        bot.send_message(message.from_user.id, 'пока')
    elif message.text == "кто лох?":
        sleep(2)
        bot.send_message(message.from_user.id, 'бекзат')
    elif message.text == "скинь ссылку":
        sleep(2)
        bot.send_message(message.from_user.id, 'https://www.youtube.com/')
    else:
        bot.send_message(message.from_user.id, '?')


bot.infinity_polling()