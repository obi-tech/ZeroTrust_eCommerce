import grpc
from concurrent import futures
import time
import account_service_pb2_grpc
from account_service_pb2_grpc import AccountServiceServicer
from account_service_pb2 import AccountRequest, AccountResponse, AccountId, DeleteResponse
from db import get_account_collection
from bson.objectid import ObjectId
from kafka_producer import publish_event
import os

class AccountService(AccountServiceServicer):
    def CreateAccount(self, request, context):
        account_collection = get_account_collection()
        account = {
            'name': request.name,
            'email': request.email,
            'password': request.password
        }
        result = account_collection.insert_one(account)
        account_id = str(result.inserted_id)
        event = {
            'event_type': 'AccountCreated',
            'account_id': account_id,
            'name': request.name,
            'email': request.email
        }
        publish_event('account-events', event)
        return AccountResponse(id=account_id, name=request.name, email=request.email)

    def GetAccount(self, request, context):
        account_collection = get_account_collection()
        account = account_collection.find_one({"_id": ObjectId(request.id)})
        if account:
            return AccountResponse(id=str(account["_id"]), name=account['name'], email=account['email'])
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Account not found')

    def UpdateAccount(self, request, context):
        account_collection = get_account_collection()
        result = account_collection.update_one(
            {"_id": ObjectId(request.id)},
            {"$set": {
                'name': request.name,
                'email': request.email,
                'password': request.password
            }}
        )
        if result.matched_count > 0:
            event = {
                'event_type': 'AccountUpdated',
                'account_id': request.id,
                'name': request.name,
                'email': request.email
            }
            publish_event('account-events', event)
            return AccountResponse(id=request.id, name=request.name, email=request.email)
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Account not found')

    def DeleteAccount(self, request, context):
        account_collection = get_account_collection()
        result = account_collection.delete_one({"_id": ObjectId(request.id)})
        if result.deleted_count > 0:
            event = {
                'event_type': 'AccountDeleted',
                'account_id': request.id
            }
            publish_event('account-events', event)
            return DeleteResponse(message='Account deleted successfully')
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Account not found')

    def GetAccountByEmail(self, request, context):
        print(request.email)
        account_collection = get_account_collection()
        account = account_collection.find_one({"email": request.email})
        if account:
            return AccountResponse(id=str(account["_id"]), name=account['name'], email=account['email'])
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Account not found')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_service_pb2_grpc.add_AccountServiceServicer_to_server(AccountService(), server)

    # Load server certificate and key
    # with open('server.crt', 'rb') as f:
    #     server_cert = f.read()
    # with open('server.key', 'rb') as f:
    #     server_key = f.read()
    # with open('ca.crt', 'rb') as f:
    #     ca_cert = f.read()
    #
    # # Configure server credentials
    # server_credentials = grpc.ssl_server_credentials(
    #     [(server_key, server_cert)],
    #     root_certificates=ca_cert,
    #     require_client_auth=True
    # )
    
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()