from kafka import KafkaConsumer
import json
from app.services.product_logic import update_stock


def consume_events():
    """Kafka Consumer to listen for order_created events."""
    consumer = KafkaConsumer(
        'order_created',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Kafka Consumer is listening for order_created events...")

    # Process Kafka messages
    for message in consumer:
        order_data = message.value
        print(f"Received order event: {order_data}")

        # Call the service function to update stock
        update_stock(order_data)
