import telebot
import os
from telebot import types



API_TOKEN = "7603459899:AAHxBgRc6JY2ES0-QGEnG1RC8dvwy6HDRFs"

bot = telebot.TeleBot(API_TOKEN)

user = {}
course_list = {
    "spring": ["ccna", "mcsa", "python"],
    "summer": ["ccna", "mcsa", "python advanced"],
    "autumn": ["icdl", "seller"],
    "winter": ["photoshaop", "linux", "c++"],
}


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Courses")
    btn2 = types.KeyboardButton("Home")
    btn3 = types.KeyboardButton("Call with Ac")
    markup.add(btn1, btn2, btn3)
    user = {}
    bot.reply_to(message, "select one our options", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_regester_course(call):
    user["course"] = call.data
    message = call.message
    text = "enter your name: "
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, base_info)

def base_info(message):
    user["info"] = message.text
    text = "enter your number: "
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, phone_info)


def phone_info(message):
    user["phone info"] = message.text
    text = "enter your phone: "
    with open("./sign.txt", "a") as file:
        for key in user:
            file.write(user[key]+"\n")
        file.write("********************")

    bot.reply_to(message, "has done")



def course(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for c in course_list:
        markup.add(types.KeyboardButton(f"{c}"))
    markup.add(types.KeyboardButton("Home"))
    bot.reply_to(message, "select one our options", reply_markup=markup)


def spring_course(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for c in course_list["spring"]:
        markup.add(types.InlineKeyboardButton(c, callback_data=c))
    bot.reply_to(message, "select one our spring course", reply_markup=markup)
    


def summer_course(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for c in course_list["summer"]:
        markup.add(types.InlineKeyboardButton(c, callback_data=c))
    bot.reply_to(message, "select one our summer course", reply_markup=markup)

def autumn_course(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for c in course_list["autumn"]:
        markup.add(types.InlineKeyboardButton(c, callback_data=c))
    bot.reply_to(message, "select one our autumn course", reply_markup=markup)

def winter_course(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for c in course_list["winter"]:
        markup.add(types.InlineKeyboardButton(c, callback_data=c))
    bot.reply_to(message, "select one our winter course", reply_markup=markup)






def call_with_ac(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Home")
    markup.add(btn1)
    bot.reply_to(message, "for call to ac this number\n**0987654321**")





@bot.message_handler(func=lambda message:True)
def call_back(message):
    if message.text == "Courses":
        course(message)

    elif message.text == "Home": 
        start(message)

    elif message.text == "Call with Ac":
        call_with_ac(message)

    elif message.text == "spring":
        user["season: "] = message.text
        spring_course(message)

    elif message.text == "summer":
        user["summer: "] = message.text
        summer_course(message)

    elif message.text == "autumn":
        user["autumn: "] = message.text
        autumn_course(message)

    elif message.text == "winter":
        user["winter: "] = message.text
        winter_course(message)





bot.infinity_polling()