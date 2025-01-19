from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_order_event(order_data):
    producer.send("order_events", value=order_data)
    print(f"Sent order event: {order_data}")
