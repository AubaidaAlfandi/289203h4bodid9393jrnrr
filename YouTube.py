import telebot
from pytube import YouTube
import time

bot = telebot.TeleBot("6475795707:AAGjAhgLux_al8QLnI5_7FODHWJ_FjbyQ28")

@bot.message_handler(func=lambda msg: True)
def download_link(message):
    try:
        link =YouTube(message.text)
        bot.reply_to(message, "يتم تحميل الفيديو !")
        print(" user "+str(message.from_user.username) +" is downloading : "+link.title)
        video = link.streams.get_highest_resolution()
        print("downloading video for "+message.from_user.username)
        video.download(filename="downloaded.mp4")
        print("uploading video for "+message.from_user.username)
        bot.send_video(message.chat.id, video=open('downloaded.mp4', 'rb'), supports_streaming=True)    
        bot.reply_to(message, "تم تحميل الفيديو بنجاح !")
    except:
        bot.reply_to(message, "ارسل رابط الفيديو")

bot.infinity_polling()