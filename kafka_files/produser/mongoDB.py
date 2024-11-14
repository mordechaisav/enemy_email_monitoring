#add conecction to mongo db
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["enemy_email"]

collection = db["all_emails"]
