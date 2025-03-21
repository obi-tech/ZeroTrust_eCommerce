# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import account_service_pb2 as account__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in account_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccount = channel.unary_unary(
                '/accountmanagement.AccountService/CreateAccount',
                request_serializer=account__service__pb2.AccountRequest.SerializeToString,
                response_deserializer=account__service__pb2.AccountResponse.FromString,
                _registered_method=True)
        self.GetAccount = channel.unary_unary(
                '/accountmanagement.AccountService/GetAccount',
                request_serializer=account__service__pb2.AccountId.SerializeToString,
                response_deserializer=account__service__pb2.AccountResponse.FromString,
                _registered_method=True)
        self.UpdateAccount = channel.unary_unary(
                '/accountmanagement.AccountService/UpdateAccount',
                request_serializer=account__service__pb2.AccountUpdateRequest.SerializeToString,
                response_deserializer=account__service__pb2.AccountResponse.FromString,
                _registered_method=True)
        self.GetAccountByEmail = channel.unary_unary(
                '/accountmanagement.AccountService/GetAccountByEmail',
                request_serializer=account__service__pb2.AccountEmail.SerializeToString,
                response_deserializer=account__service__pb2.AccountResponse.FromString,
                _registered_method=True)
        self.DeleteAccount = channel.unary_unary(
                '/accountmanagement.AccountService/DeleteAccount',
                request_serializer=account__service__pb2.AccountId.SerializeToString,
                response_deserializer=account__service__pb2.DeleteResponse.FromString,
                _registered_method=True)


class AccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountByEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=account__service__pb2.AccountRequest.FromString,
                    response_serializer=account__service__pb2.AccountResponse.SerializeToString,
            ),
            'GetAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccount,
                    request_deserializer=account__service__pb2.AccountId.FromString,
                    response_serializer=account__service__pb2.AccountResponse.SerializeToString,
            ),
            'UpdateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccount,
                    request_deserializer=account__service__pb2.AccountUpdateRequest.FromString,
                    response_serializer=account__service__pb2.AccountResponse.SerializeToString,
            ),
            'GetAccountByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountByEmail,
                    request_deserializer=account__service__pb2.AccountEmail.FromString,
                    response_serializer=account__service__pb2.AccountResponse.SerializeToString,
            ),
            'DeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccount,
                    request_deserializer=account__service__pb2.AccountId.FromString,
                    response_serializer=account__service__pb2.DeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'accountmanagement.AccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('accountmanagement.AccountService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AccountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/accountmanagement.AccountService/CreateAccount',
            account__service__pb2.AccountRequest.SerializeToString,
            account__service__pb2.AccountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/accountmanagement.AccountService/GetAccount',
            account__service__pb2.AccountId.SerializeToString,
            account__service__pb2.AccountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/accountmanagement.AccountService/UpdateAccount',
            account__service__pb2.AccountUpdateRequest.SerializeToString,
            account__service__pb2.AccountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAccountByEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/accountmanagement.AccountService/GetAccountByEmail',
            account__service__pb2.AccountEmail.SerializeToString,
            account__service__pb2.AccountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/accountmanagement.AccountService/DeleteAccount',
            account__service__pb2.AccountId.SerializeToString,
            account__service__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
