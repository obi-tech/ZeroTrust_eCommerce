from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(topic, event):
    producer.send(topic, event)
    producer.flush()