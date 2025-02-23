from pymongo import MongoClient
import os
# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["order_management"]

def get_order_collection():
    return db["orders"]
