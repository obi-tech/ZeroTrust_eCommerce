from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["account_management"]

def get_account_collection():
    return db["accounts"]