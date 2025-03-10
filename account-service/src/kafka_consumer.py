import os

from kafka import KafkaConsumer
import json
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
consumer = KafkaConsumer(
    'account-events',
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    api_version=(3, 5, 0),
    group_id='account-service-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    event = message.value
    print(f"Received event: {event}")