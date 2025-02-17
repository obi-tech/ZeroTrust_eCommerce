from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27016/"  # Change if needed
client = MongoClient(MONGO_URI)
db = client["product-inventory"]
products_collection = db["products"]

def get_product_collection():
    return products_collection
