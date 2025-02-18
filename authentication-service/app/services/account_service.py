import grpc
from . import account_service_pb2
from . import account_service_pb2_grpc
from flask import current_app

def get_account_stub():
    channel = grpc.insecure_channel(current_app.config['GRPC_SERVER_ADDRESS'])
    return account_service_pb2_grpc.AccountServiceStub(channel)

def create_account(name, email, password):
    stub = get_account_stub()
    request = account_service_pb2.AccountRequest(name=name, email=email, password=password)
    response = stub.CreateAccount(request)
    return response

def get_account(account_id):
    stub = get_account_stub()
    request = account_service_pb2.AccountId(id=account_id)
    response = stub.GetAccount(request)
    return response

def get_account_by_email(account_email):
    print(account_email)
    stub = get_account_stub()
    request = account_service_pb2.AccountEmail(email=account_email)
    response = stub.GetAccountByEmail(request)
    return response

def update_account(account_id, name, email, password):
    stub = get_account_stub()
    request = account_service_pb2.AccountUpdateRequest(id=account_id, name=name, email=email, password=password)
    response = stub.UpdateAccount(request)
    return response

def delete_account(account_id):
    stub = get_account_stub()
    request = account_service_pb2.AccountId(id=account_id)
    response = stub.DeleteAccount(request)
    return response