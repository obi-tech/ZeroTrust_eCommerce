from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'account-events',
    bootstrap_servers='localhost:9093',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='account-service-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    event = message.value
    print(f"Received event: {event}")