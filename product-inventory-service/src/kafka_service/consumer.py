import os

from kafka import KafkaConsumer
import json
from src.services.product_logic import update_stock

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
def consume_events():
    """Kafka Consumer to listen for order_created events."""
    print(f"KAFKA_BROKER: ", KAFKA_BROKER)

    consumer = KafkaConsumer(
        'order_created',
        bootstrap_servers=KAFKA_BROKER,
        api_version=(3, 5, 0),
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )


    print("Kafka Consumer is listening for order_created events...")

    # Process Kafka messages
    for message in consumer:
        order_data = message.value
        print(f"Received order event: {order_data}")

        # Call the service function to update stock
        update_stock(order_data)
