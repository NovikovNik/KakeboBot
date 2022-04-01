from telebot import types

def get_start_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Начать настройку')
    itembtn2 = types.KeyboardButton('Удалить свою информацию')
    itembtn3 = types.KeyboardButton('Информация')
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup

def get_settings_menu():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Отменить настройку')
    markup.add(itembtn1)
    return types.ReplyKeyboardRemove()