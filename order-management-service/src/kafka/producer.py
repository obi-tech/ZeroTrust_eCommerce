from kafka import KafkaProducer
import json
import os

KAFKA_BROKER = os.getenv("KAFKA_BROKER")  # Use Docker service name
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    api_version=(3, 5, 0),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    request_timeout_ms = 120000,
    metadata_max_age_ms = 120000
)
print(f"Kafka producer created for broker: {KAFKA_BROKER}")

# create_kafka_topic('order_created')

def send_order_event(order_data):
    producer.send("order_created", value=order_data)
    print(f"Sent order event: {order_data}")
# Example payload for order. create_date will be updated with current date so dont have to pass
# {
# "product_id": "P78624",
# "quantity": 70,
# "created_by": "U193039"
# }


