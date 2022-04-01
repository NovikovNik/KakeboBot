from telebot import types

def get_start_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать настройку", callback_data="cb_settings"),
                               types.InlineKeyboardButton("Информация", callback_data="cb_info"))
    return markup

def get_settings_menu():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Отменить настройку')
    markup.add(itembtn1)
    return types.ReplyKeyboardRemove()