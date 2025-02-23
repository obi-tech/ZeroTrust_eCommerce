import pandas as pd
from pymongo import MongoClient
from .config_db import COLLECTION_NAME, MONGO_URI, DB_NAME

csv_file = 'src/db/products.csv'
df = pd.read_csv(csv_file)
data = df.to_dict(orient="records")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
products_collection = db[COLLECTION_NAME]

# Insert dummy data into MongoDB
if data:
    products_collection.insert_many(data)
    print(f"{len(data)} products imported successfully into MongoDB!")
else:
    print("No data found in CSV file.")

def get_product_collection():
    return products_collection