# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stamp_reflector_pb2 as stamp__reflector__pb2


class STAMPSessionReflectorServiceStub(object):
    """STAMPSessionReflectorService provides RPCs used to control a STAMP Session
    Reflector
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/Init',
                request_serializer=stamp__reflector__pb2.InitStampReflectorRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.InitStampReflectorReply.FromString,
                )
        self.Reset = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/Reset',
                request_serializer=stamp__reflector__pb2.ResetStampReflectorRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.ResetStampReflectorReply.FromString,
                )
        self.CreateStampSession = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/CreateStampSession',
                request_serializer=stamp__reflector__pb2.CreateStampReflectorSessionRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.CreateStampReflectorSessionReply.FromString,
                )
        self.StartStampSession = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/StartStampSession',
                request_serializer=stamp__reflector__pb2.StartStampReflectorSessionRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.StartStampReflectorSessionReply.FromString,
                )
        self.StopStampSession = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/StopStampSession',
                request_serializer=stamp__reflector__pb2.StopStampReflectorSessionRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.StopStampReflectorSessionReply.FromString,
                )
        self.DestroyStampSession = channel.unary_unary(
                '/srv6pm.STAMPSessionReflectorService/DestroyStampSession',
                request_serializer=stamp__reflector__pb2.DestroyStampReflectorSessionRequest.SerializeToString,
                response_deserializer=stamp__reflector__pb2.DestroyStampReflectorSessionReply.FromString,
                )


class STAMPSessionReflectorServiceServicer(object):
    """STAMPSessionReflectorService provides RPCs used to control a STAMP Session
    Reflector
    """

    def Init(self, request, context):
        """Init: RPC used to initialize the Session Sender
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Reset: RPC used to initialize the Session Sender
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStampSession(self, request, context):
        """CreateStampSession: RPC used to create a STAMP Session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartStampSession(self, request, context):
        """StartStampSession: RPC used to start a STAMP Session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopStampSession(self, request, context):
        """StopStampSession: RPC used to stop a STAMP Session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyStampSession(self, request, context):
        """DestroyStampSession: RPC used to destroy an existing STAMP Session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_STAMPSessionReflectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=stamp__reflector__pb2.InitStampReflectorRequest.FromString,
                    response_serializer=stamp__reflector__pb2.InitStampReflectorReply.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=stamp__reflector__pb2.ResetStampReflectorRequest.FromString,
                    response_serializer=stamp__reflector__pb2.ResetStampReflectorReply.SerializeToString,
            ),
            'CreateStampSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStampSession,
                    request_deserializer=stamp__reflector__pb2.CreateStampReflectorSessionRequest.FromString,
                    response_serializer=stamp__reflector__pb2.CreateStampReflectorSessionReply.SerializeToString,
            ),
            'StartStampSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StartStampSession,
                    request_deserializer=stamp__reflector__pb2.StartStampReflectorSessionRequest.FromString,
                    response_serializer=stamp__reflector__pb2.StartStampReflectorSessionReply.SerializeToString,
            ),
            'StopStampSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StopStampSession,
                    request_deserializer=stamp__reflector__pb2.StopStampReflectorSessionRequest.FromString,
                    response_serializer=stamp__reflector__pb2.StopStampReflectorSessionReply.SerializeToString,
            ),
            'DestroyStampSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyStampSession,
                    request_deserializer=stamp__reflector__pb2.DestroyStampReflectorSessionRequest.FromString,
                    response_serializer=stamp__reflector__pb2.DestroyStampReflectorSessionReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'srv6pm.STAMPSessionReflectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class STAMPSessionReflectorService(object):
    """STAMPSessionReflectorService provides RPCs used to control a STAMP Session
    Reflector
    """

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/Init',
            stamp__reflector__pb2.InitStampReflectorRequest.SerializeToString,
            stamp__reflector__pb2.InitStampReflectorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/Reset',
            stamp__reflector__pb2.ResetStampReflectorRequest.SerializeToString,
            stamp__reflector__pb2.ResetStampReflectorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStampSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/CreateStampSession',
            stamp__reflector__pb2.CreateStampReflectorSessionRequest.SerializeToString,
            stamp__reflector__pb2.CreateStampReflectorSessionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartStampSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/StartStampSession',
            stamp__reflector__pb2.StartStampReflectorSessionRequest.SerializeToString,
            stamp__reflector__pb2.StartStampReflectorSessionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopStampSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/StopStampSession',
            stamp__reflector__pb2.StopStampReflectorSessionRequest.SerializeToString,
            stamp__reflector__pb2.StopStampReflectorSessionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyStampSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.STAMPSessionReflectorService/DestroyStampSession',
            stamp__reflector__pb2.DestroyStampReflectorSessionRequest.SerializeToString,
            stamp__reflector__pb2.DestroyStampReflectorSessionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
