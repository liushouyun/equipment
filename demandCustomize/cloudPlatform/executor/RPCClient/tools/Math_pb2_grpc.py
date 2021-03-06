# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import Math_pb2 as Math__pb2


class MathStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sum = channel.unary_unary(
        '/tools.Math/sum',
        request_serializer=Math__pb2.SerializedIOStream.SerializeToString,
        response_deserializer=Math__pb2.SerializedIOStream.FromString,
        )


class MathServicer(object):

  def sum(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MathServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sum': grpc.unary_unary_rpc_method_handler(
          servicer.sum,
          request_deserializer=Math__pb2.SerializedIOStream.FromString,
          response_serializer=Math__pb2.SerializedIOStream.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tools.Math', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
