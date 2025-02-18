import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    GRPC_SERVER_ADDRESS = os.environ.get('GRPC_SERVER_ADDRESS') or 'localhost:50051'
    JWT_EXPIRATION_HOURS = 24