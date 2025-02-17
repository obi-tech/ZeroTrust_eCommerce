from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Simulated Order Event
order_event = {
    "product_id": "P78624",
    "quantity": 2,
    "price": 1000
}

producer.send("order_created", order_event)
print("Order event sent!")
