from datetime import date, datetime
from unicodedata import name
from sqlalchemy.orm import Session
import models
from database import get_db
# from main import bot


# def check_registration(user_id, chat_id):
#     db = get_db()
#     user = db.query(models.User).filter(models.User.name == user_id).first()
#     db.close()
#     if user:
#         return True
#     else: bot.send_message(chat_id, text="""Привет! Ты еще не авторизовался в приложении!
#                            Для начала работы набери команду /start""")

def set_settings_state(user_id, state):
    db = get_db()
    db.query(models.User).filter(models.User.name == user_id).update({models.User.settings_state:state}, synchronize_session=False)
    db.commit()
    db.close()

def get_settings_state(user_id):
    db = get_db()
    user = db.query(models.User).filter(models.User.name == user_id).first()
    return user.settings_state

def initial_user_create(user_name, nick, chat_id):
    db = get_db()
    
    new_user = models.User(name=user_name, 
                           first_authorization=datetime.now(), 
                           nick_name=nick, 
                           chat_id=chat_id,
                           settings_state=0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    
def find_user_in_db(user_id):
    db = get_db()
    
    user = db.query(models.User).filter(models.User.name == user_id).first()
    db.close()
    return user