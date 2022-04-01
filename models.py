import sqlite3
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    chat_id = Column(String)
    nick_name = Column(String)
    first_authorization = Column(String)
    settings_state = Column(Integer)
    
class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    money_incam = Column(Integer)
    expenses = Column(String)
    percent = Column(Integer)
    