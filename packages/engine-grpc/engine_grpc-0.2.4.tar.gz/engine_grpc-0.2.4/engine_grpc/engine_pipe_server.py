from concurrent import futures
import grpc
from ugrpc_pipe import ugrpc_pipe_pb2
from ugrpc_pipe import ugrpc_pipe_pb2_grpc


class UGrpcPipeImpl(ugrpc_pipe_pb2_grpc.UGrpcPipeServicer):
    def CommandParser(self, request, context):
        print("CommandParser")
        print(request.payload)
        print(context)
        status = ugrpc_pipe_pb2.Status(code=0, message="OK")
        return ugrpc_pipe_pb2.GenericResp(status=status, payload={})


def run_grpc_server(service_impl: type = UGrpcPipeImpl, port: int = 50061) -> None:

    if not issubclass(service_impl, ugrpc_pipe_pb2_grpc.UGrpcPipeServicer):
        raise TypeError(
            f"service_impl must be a subclass of {ugrpc_pipe_pb2_grpc.UGrpcPipeServicer}")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ugrpc_pipe_pb2_grpc.add_UGrpcPipeServicer_to_server(
        service_impl(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print("server started")
    server.wait_for_termination()
