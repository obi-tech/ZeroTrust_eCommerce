import os

from kafka import KafkaProducer
import json

KAFKA_BROKER = os.getenv("KAFKA_BROKER")  # Use Docker service name
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    api_version=(3, 5, 0),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    request_timeout_ms = 120000,
    metadata_max_age_ms = 120000
)

def publish_event(topic, event):
    producer.send(topic, event)
    producer.flush()