import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27016/"
DB_NAME = "product-inventory"
COLLECTION_NAME = "products"

# Load CSV data
csv_file = "products.csv"  # Ensure the CSV file is in the same directory
df = pd.read_csv(csv_file)

# Convert DataFrame to dictionary format
data = df.to_dict(orient="records")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
products_collection = db[COLLECTION_NAME]

# Insert data into MongoDB
if data:
    products_collection.insert_many(data)
    print(f"{len(data)} products imported successfully into MongoDB!")
else:
    print("No data found in CSV file.")
