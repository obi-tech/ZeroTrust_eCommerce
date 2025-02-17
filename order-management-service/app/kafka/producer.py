from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_order_event(order_data):
    producer.send("order_created", value=order_data)
    print(f"Sent order event: {order_data}")

# Example payload for order. create_date will be updated with current date so dont have to pass
# {
# "product_id": "P78624",
# "quantity": 70,
# "created_by": "U193039"
# }

