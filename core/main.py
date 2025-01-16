import telebot
import os
from telebot import types



API_TOKEN = "7603459899:AAHxBgRc6JY2ES0-QGEnG1RC8dvwy6HDRFs"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Courses")
    btn2 = types.KeyboardButton("Home")
    btn3 = types.KeyboardButton("Call with Ac")
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, "select one our options", reply_markup=markup)



bot.infinity_polling()