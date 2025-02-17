import grpc
from app.grpc_service.auth_pb2 import ValidateTokenRequest
from app.grpc_service.auth_pb2_grpc import AuthServiceStub

class AuthClient:
    def __init__(self, host="localhost", port=50051):
        """
        Initialize the gRPC client for the authentication service.

        :param host: Hostname of the authentication service.
        :param port: Port of the authentication service.
        """
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = AuthServiceStub(self.channel)

    def validate_token(self, token):
        """
        Validate the provided token with the authentication service.

        :param token: The user token to validate.
        :return: A tuple (is_valid, username). `is_valid` is a boolean indicating
                 whether the token is valid, and `username` is the associated username
                 if valid.
        """
        try:
            request = ValidateTokenRequest(token=token)
            response = self.stub.ValidateToken(request)
            return response.is_valid, response.username
        except grpc.RpcError as e:
            # Handle gRPC errors, e.g., connection issues or invalid token response
            print(f"gRPC error: {e.details()}")
            return False, None
