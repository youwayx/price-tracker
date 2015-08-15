from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
if not os.environ.get('POSTGRES_URL', None):
	from secrets import POSTGRES_URL
else:
	POSTGRES_URL = os.environ.get('POSTGRES_URL')

engine = create_engine(POSTGRES_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Item(Base):
	__tablename__ = 'items'
	id = Column(Integer, primary_key=True)
	url = Column(String(200), unique=True)
	price = Column(Integer)

	def __init__(self, url, price):
		self.url = url
		self.price = price


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	email = Column(String(200), unique=True)

	def __init__(self, email):
		self.email = email


class Transaction(Base):
	__tablename__ = 'transactions'

	id = Column(Integer, primary_key=True)
	item_id = Column(Integer)
	user_id = Column(Integer)
	requested_price = Column(Integer)

	def __init__(self, item_id, user_id, requested_price):
		self.item_id = item_id
		self.user_id = user_id
		self.requested_price = requested_price

def init():
	Base.metadata.create_all(engine)
