import grpc
from concurrent import futures
import auth_pb2
import auth_pb2_grpc
from app.services.auth_logic import generate_token, validate_token

class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Login(self, request, context):
        if request.username == "admin" and request.password == "password":
            token = generate_token(request.username)
            return auth_pb2.LoginResponse(token=token)
        context.set_code(grpc.StatusCode.UNAUTHENTICATED)
        context.set_details("Invalid username or password")
        return auth_pb2.LoginResponse()

    def ValidateToken(self, request, context):
        is_valid, username = validate_token(request.token)
        if is_valid:
            return auth_pb2.ValidateTokenResponse(valid=True, username=username)
        context.set_code(grpc.StatusCode.UNAUTHENTICATED)
        context.set_details(username)  # username contains the error
        return auth_pb2.ValidateTokenResponse(valid=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
