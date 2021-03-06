from email import message
from lib2to3.pytree import Base
from repo import bot_repo
from models import *
from database import *
from user import *
import telebot
from telebot import types

if debug:=True == True:
    Base.metadata.drop_all(engine) ##Убрать позже
Base.metadata.create_all(engine)
database = get_db()

token = ""
bot = telebot.TeleBot(token, parse_mode=None)

hideBoard = types.ReplyKeyboardRemove()

@bot.message_handler(commands=['start'])
def initialising(message):
    chat = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.first_name
    user = find_user_in_db(user_id)
    if not user:
        bot.reply_to(message, f"Привет, {username}! Мы с тобой еще на знакомы, я Kekebo me -- бот, который позволяет грамотно отслеживать свои повседневные расходы.")
        initial_user_create(user_name=user_id, nick=username, chat_id=chat)
        bot.send_message(chat_id=chat, text="Добавил тебя в свою базу данных!")
        bot.send_message(chat_id=chat, text="Для начала пользования нужно заполнить некоторые данные, такие как расходы и приходы, сделать это можно в настройках.")
        base_bot_menu(chat)
    else:
        bot.reply_to(message, f"Привет, {username} ты уже зарегестрирован в системе! Если хочешь удалить свои данные, перейди в настройки!")
        base_bot_menu(chat)
    
def base_bot_menu(chat_id):
    bot.send_message(chat_id, text="Выбери действие:", reply_markup=bot_repo.get_start_menu())

# @bot.message_handler(func=lambda message: message.text == "Начать настройку")
# def settings(message):
#     chat = message.chat.id
#     bot.send_message(chat_id=chat, text="Приступим", reply_markup=hideBoard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat = call.message.chat.id
    if call.data == "cb_settings":
        # bot.answer_callback_query(call.id, "Приступим")
        bot.send_message(chat_id=chat, text="Приступим.\n[1] Для начала напиши свой месячный заработок: ", reply_markup=hideBoard)
        set_settings_state(user_id=chat, state=1)
    elif call.data == "cb_info":
        bot.send_message(chat_id=chat, text="В разработке..", reply_markup=hideBoard)
    
@bot.message_handler(func=lambda message: message.text.isdigit() == True)
def set_money_values(message):
    user = message.chat.id
    if get_settings_state(user) == 1:
        bot.send_message(message.chat.id, text=("Отлично, с зарплатой разобрались.\n[2] Теперь напиши сколько денег уходит на обязательные траты: коммунальные услуги, подписки, кредиты, рассрочки."))
        set_settings_state(user_id=user, state=2)

bot.infinity_polling()