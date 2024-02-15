import telebot as tb
import re

from core import viewbot
from core import dataprovider as dprovider
from datas.configs import *
from core import presenters

TOKEN = input("input token your bot >> ")

bot = tb.TeleBot(TOKEN, parse_mode="MARKDOWN")

@bot.message_handler(commands=['start'])
def start(message):
    markup = viewbot.create_main_menu()
    bot.send_message(message.chat.id, MESSAGES["start"], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == DEV_COMMANDS["show_recipe"])
def show_recipe_of_id_callback(call):
    
    markup = viewbot.create_main_remove()

    bot.send_message(call.message.chat.id, MESSAGES["show_recipe"], reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data == DEV_COMMANDS["show_all"])
def show_all_recipe_callback(call):
    response = dprovider.provide_all_recipes()
    recipe_formatter = presenters.create_formatter_recipe(*response)

    markup = viewbot.create_main_menu()

    bot.send_message(call.message.chat.id, recipe_formatter.get_head(), reply_markup=markup)

@bot.message_handler(content_types=["text"], func=lambda m: re.fullmatch(r'\d', m.text))
def show_recipe(message):
    response = dprovider.provide_recipe_of_id(int(message.text))
    recipe_formatter = presenters.create_formatter_recipe(response)

    markup = viewbot.create_main_menu()

    bot.send_message(message.chat.id, recipe_formatter.get_full())
    
    with open(r"resources\img0.png", "rb") as f_img:
        bot.send_sticker(message.chat.id, f_img, reply_markup=markup) 


if __name__ == "__main__":
    bot.infinity_polling()




