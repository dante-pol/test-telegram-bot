
from telebot import types

def create_main_menu():
        from datas.configs import MESSAGES, DEV_COMMANDS, TEXT_UI

        markup = types.InlineKeyboardMarkup()

        btn_show_recipe = types.InlineKeyboardButton(text= TEXT_UI["get_recipe"], callback_data=DEV_COMMANDS["show_recipe"])
        btn_show_all_recipe = types.InlineKeyboardButton(text= TEXT_UI["get_all_recipe"], callback_data= DEV_COMMANDS["show_all"])
        
        btnAdd = types.InlineKeyboardButton(text= TEXT_UI["add_new_recipe"], callback_data= DEV_COMMANDS["add_recipe"])


        markup.row(btn_show_recipe, btn_show_all_recipe)
        markup.row(btnAdd)

        return markup


def create_main_remove():
        
        markup = types.ReplyKeyboardRemove()

        return markup