from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
crashes_db = client['crashes-data']

daily = crashes_db['daily_data']
monthly = crashes_db['monthly_data']
weekly = crashes_db['weekly_data']
areas = crashes_db['areas']
accidents = crashes_db['accidents']