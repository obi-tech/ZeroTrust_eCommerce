import grpc
import jwt
import account_service_pb2
import account_service_pb2_grpc

SECRET_KEY = 'your_secret_key'

def generate_token():
    payload = {
        'user_id': '123',
        'role': 'admin'
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def create_channel():
    with open('client.crt', 'rb') as f:
        client_cert = f.read()
    with open('client.key', 'rb') as f:
        client_key = f.read()
    with open('ca.crt', 'rb') as f:
        ca_cert = f.read()

    credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert,
        private_key=client_key,
        certificate_chain=client_cert
    )

    channel = grpc.secure_channel('localhost:50051', credentials)
    return channel

def create_account(name, email, password):
    token = generate_token()
    channel = create_channel()
    stub = account_service_pb2_grpc.AccountServiceStub(channel)

    metadata = [('authorization', token)]
    request = account_service_pb2.AccountRequest(name=name, email=email, password=password)
    response = stub.CreateAccount(request, metadata=metadata)
    print(response)

def test_create_multiple_accounts():
    users = [
        {"name": "Alice Smith", "email": "alice@example.com", "password": "password1"},
        {"name": "Bob Johnson", "email": "bob@example.com", "password": "password2"},
        {"name": "Charlie Brown", "email": "charlie@example.com", "password": "password3"},
        {"name": "Diana Prince", "email": "diana@example.com", "password": "password4"},
    ]

    for user in users:
        create_account(user["name"], user["email"], user["password"])

def test_invalid_token():
    token = 'invalid_token'
    channel = create_channel()
    stub = account_service_pb2_grpc.AccountServiceStub(channel)

    metadata = [('authorization', token)]
    request = account_service_pb2.AccountRequest(name='John Doe', email='john@example.com', password='password')
    try:
        response = stub.CreateAccount(request, metadata=metadata)
    except grpc.RpcError as e:
        print(e.details())

def test_no_token():
    channel = create_channel()
    stub = account_service_pb2_grpc.AccountServiceStub(channel)

    request = account_service_pb2.AccountRequest(name='John Doe', email='john@example.com', password='password')
    try:
        response = stub.CreateAccount(request)
    except grpc.RpcError as e:
        print(e.details())

if __name__ == '__main__':
    test_create_multiple_accounts()
    test_invalid_token()
    test_no_token()