from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["order_management"]

def get_order_collection():
    return db["orders"]
