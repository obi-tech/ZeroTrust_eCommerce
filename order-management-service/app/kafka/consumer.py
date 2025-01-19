from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "order_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

def process_order_events():
    for message in consumer:
        order_event = message.value
        print(f"Processing order event: {order_event}")
