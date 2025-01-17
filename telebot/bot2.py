import telebot

TOKEN = '7273022293:AAHj8RbzHx__iBgWnjdNJlf7ejLXr159irw'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('ERA69')
    button2 = telebot.types.KeyboardButton('Video-Nike')
    button3 = telebot.types.KeyboardButton('Help')
    button4 = telebot.types.KeyboardButton('Audio') 
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'ERA69')
def send_nike(message):
    with open('image1.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")

@bot.message_handler(func=lambda message: message.text == 'Video-Nike')
def send_video_nike(message):
    with open('NIKE - COMMERCIAL - 2024 -  JUST DO IT - AI ENTERTAINMENT.mp4', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео.")

@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")

@bot.message_handler(func=lambda message: message.text == 'Audio')
def send_audio(message):
    with open('АДЛИН - No Love.mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

bot.polling()

