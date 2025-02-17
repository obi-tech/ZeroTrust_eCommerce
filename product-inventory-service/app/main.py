from app.grpc_service.grpc_server import serve
from app.kafka_service.consumer import consume_events
import threading

def start_kafka_consumer():
    consume_events()  # Run Kafka consumer

if __name__ == "__main__":
    # Start Kafka consumer in a separate thread
    kafka_thread = threading.Thread(target=start_kafka_consumer, daemon=True)
    kafka_thread.start()

    # Start gRPC server
    serve()
