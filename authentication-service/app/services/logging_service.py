import grpc
from . import logging_pb2
from . import logging_pb2_grpc
import time

class LoggingClient:
    def __init__(self, host='localhost', port=50055):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = logging_pb2_grpc.LoggingServiceStub(self.channel)

    def send_log(self, service, level, message):
        log_request = logging_pb2.LogRequest(
            service=service,
            level=level,
            message=message,
            timestamp=time.time()
        )
        try:
            response = self.stub.SendLog(log_request)
            print(f"Log sent with ID: {response}")
            return response.id
        except grpc.RpcError as e:
            print(f"An error occurred: {e.details()}")
            return None

