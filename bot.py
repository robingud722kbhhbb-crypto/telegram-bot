import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# ТЕКСТ
@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, "Текст получил!")

# ФОТО
@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    bot.send_message(message.chat.id, "Фото получил!")

# ВИДЕО
@bot.message_handler(content_types=['video'])
def video_handler(message):
    bot.send_message(message.chat.id, "Видео получил!")

# ГОЛОСОВОЕ
@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    bot.send_message(message.chat.id, "Голосовое получил!")

# ДОКУМЕНТЫ
@bot.message_handler(content_types=['document'])
def document_handler(message):
    bot.send_message(message.chat.id, "Документ получил!")

# СТИКЕРЫ
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    bot.send_message(message.chat.id, "Стикер получил!")

bot.polling(none_stop=True)
