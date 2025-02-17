from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_event(topic, event_data):
    producer.send(topic, event_data)
    print(f"Published event to topic '{topic}': {event_data}")
