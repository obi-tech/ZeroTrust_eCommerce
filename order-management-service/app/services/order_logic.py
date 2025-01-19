from app.services.db import get_order_collection
from ..kafka.producer import send_order_event
from bson import ObjectId
from bson.errors import InvalidId

# Initialize the orders collection
orders = get_order_collection()


# Helper function to convert ObjectId to string for JSON serialization
def convert_objectid_to_str(data):
    if isinstance(data, dict):
        # Recursively convert each value in the dictionary
        return {key: convert_objectid_to_str(value) for key, value in data.items()}
    elif isinstance(data, list):
        # Recursively convert each item in the list
        return [convert_objectid_to_str(item) for item in data]
    elif isinstance(data, ObjectId):
        # Convert ObjectId to string
        return str(data)
    else:
        # Leave other data types unchanged
        return data


# Function to create a new order
def create_order(order_data):
    # Ensure unique _id: Remove if it already exists
    order_data.pop("_id", None)

    # Insert order into MongoDB
    try:
        result = orders.insert_one(order_data)
        order_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string for external usage

        print(f"Inserted order with _id: {result.inserted_id}")

        # Send Kafka event
        send_order_event(order_data)

        return order_data  # Return order data with string _id

    except Exception as e:
        # Handle unexpected errors during insertion
        print(f"Error creating order: {str(e)}")
        return {"error": "An unexpected error occurred while creating the order"}


# Function to retrieve an order by its ID
def get_order(order_id: str):
    try:
        # Convert order_id to ObjectId for MongoDB query
        order = orders.find_one({"_id": ObjectId(order_id)})

        # If no order is found, return an error
        if not order:
            return {"error": "Order not found"}

        # Convert ObjectId fields in the document to strings
        return convert_objectid_to_str(order)

    except InvalidId:
        # Handle invalid ObjectId format
        return {"error": "Invalid order ID format"}

    except Exception as e:
        # Handle unexpected errors during retrieval
        print(f"Error retrieving order: {str(e)}")
        return {"error": "An unexpected error occurred while retrieving the order"}


def delete_order(order_id: str):
    try:
        # Convert order_id to ObjectId
        result = orders.delete_one({"_id": ObjectId(order_id)})

        # Check if any document was deleted
        if result.deleted_count == 0:
            return {"error": "Order not found"}

        return {"message": "Order deleted successfully"}

    except InvalidId:
        # Handle invalid ObjectId format
        return {"error": "Invalid order ID format"}

    except Exception as e:
        # Handle unexpected errors
        print(f"Error deleting order: {str(e)}")
        return {"error": "An unexpected error occurred while deleting the order"}

def update_order(order_id: str, update_data: dict):
    try:
        # Ensure _id is not being updated
        update_data.pop("_id", None)

        # Convert order_id to ObjectId
        result = orders.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": update_data}  # Only update the provided fields
        )

        # Check if any document was updated
        if result.matched_count == 0:
            return {"error": "Order not found"}

        return {"message": "Order updated successfully"}

    except InvalidId:
        # Handle invalid ObjectId format
        return {"error": "Invalid order ID format"}

    except Exception as e:
        # Handle unexpected errors
        print(f"Error updating order: {str(e)}")
        return {"error": "An unexpected error occurred while updating the order"}

