import grpc
import logging
import grpc_cotea.cotea_pb2_grpc as cotea_pb2_grpc

from concurrent import futures
from grpc_cotea.cotea_gateway import CoteaGatewayServicer


class CoteaGatewayServer:
    def __init__(self, workers_connecter, port, host=None, log_lvl=logging.INFO, workers=None, workers_count=5, workers_killing_timeout=300):
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        cotea_gateway_servicer = CoteaGatewayServicer(workers_connecter, gateway_port=self.port, log_lvl=log_lvl, \
             workers=workers, initial_worker_count=workers_count, workers_killing_timeout=workers_killing_timeout)
        cotea_pb2_grpc.add_CoteaGatewayServicer_to_server(cotea_gateway_servicer, self.server)

        host_str = "localhost"
        if host:
            host_str = host
        self.host = host_str
        self.server.add_insecure_port(host_str + ":" + port)
    
    def start(self):
        starting_at = self.host + ":" + self.port
        print("starting grpc-cotea gateway at {}".format(starting_at))
        self.server.start()
        self.server.wait_for_termination()
