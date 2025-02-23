from src.grpc_service.grpc_server import serve
from src.kafka_service.consumer import consume_events
import threading


if __name__ == "__main__":
    consume_events()  # Run Kafka consumer

    # Start Kafka consumer in a separate thread
    # kafka_thread = threading.Thread(target=start_kafka_consumer, daemon=True)
    # kafka_thread.start()

    # Start gRPC server
    serve()
