from pymongo.errors import DuplicateKeyError

from ..db.db import get_product_collection

# Get MongoDB collection
products_collection = get_product_collection()

def update_stock(order):
    """Update product stock when an order is received, ensuring stock is available."""
    product_id = order["product_id"]
    quantity = order["quantity"]

    # Fetch the current stock
    product = products_collection.find_one({"product_id": product_id})

    if not product:
        print(f"❌ Product {product_id} not found!")
        return {"error": "Product not found"}, 404

    # Check if stock is sufficient
    if product["stock"] < quantity:
        print(f"❌ Not enough stock for {product_id}. Requested: {quantity}, Available: {product['stock']}")
        return {"error": "Not enough stock"}, 400

    # If stock is available, update it
    result = products_collection.update_one(
        {"product_id": product_id},
        {"$inc": {"stock": -quantity}}  # Reduce stock
    )

    if result.modified_count > 0:
        print(f"✅ Stock updated for {product_id}: -{quantity}")
        return {"success": True}, 200
    else:
        print(f"⚠️ Failed to update stock for {product_id}")
        return {"error": "Failed to update stock"}, 500

def add_product(product_id: str, name: str, price: float, stock: int):
    """Adds a new product to the database."""
    try:
        product = {
            "product_id": product_id,
            "name": name,
            "price": price,
            "stock": stock
        }
        products_collection.insert_one(product)
        print(f"✅ Product {product_id} added successfully!")
        return product
    except DuplicateKeyError:
        print(f"⚠️ Product {product_id} already exists!")
        return None

# 🚀 2️⃣ Get a Product by ID
def get_product(product_id: str):
    """Fetches a product by product_id."""
    product = products_collection.find_one({"product_id": product_id}, {"_id": 0})  # Exclude MongoDB _id
    if product:
        return product
    else:
        print(f"⚠️ Product {product_id} not found!")
        return None

# 🚀 3️⃣ Update a Product
def update_product(product_id: str, name=None, price=None, stock=None):
    """Updates a product's details in the database."""
    update_fields = {}

    if name:
        update_fields["name"] = name
    if price:
        update_fields["price"] = price
    if stock is not None:  # Stock can be zero
        update_fields["stock"] = stock

    if update_fields:
        result = products_collection.update_one(
            {"product_id": product_id},
            {"$set": update_fields}
        )
        if result.matched_count > 0:
            print(f"✅ Product {product_id} updated successfully!")
            return True
        else:
            print(f"⚠️ Product {product_id} not found!")
            return False
    else:
        print("⚠️ No fields provided for update!")
        return False

# 🚀 4️⃣ Delete a Product
def delete_product(product_id: str):
    """Deletes a product from the database."""
    result = products_collection.delete_one({"product_id": product_id})
    if result.deleted_count > 0:
        print(f"✅ Product {product_id} deleted successfully!")
        return True
    else:
        print(f"⚠️ Product {product_id} not found!")
        return False
