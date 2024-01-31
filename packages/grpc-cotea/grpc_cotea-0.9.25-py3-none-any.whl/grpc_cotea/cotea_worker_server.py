import grpc
import grpc_cotea.cotea_pb2_grpc as cotea_pb2_grpc

from concurrent import futures
from grpc_cotea.cotea_worker import CoteaWorkerServicer


class CoteaWorkerServer:
    def __init__(self, port, logging_lbl="worker", grpc_server=None, use_mitogen=False, merge_logs=True):
        self.port = port
        self.logging_lbl = logging_lbl

        if grpc_server:
            self.server = grpc_server
        else:
            self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

        cotea_worker_servicer = CoteaWorkerServicer(logging_lbl=logging_lbl, use_mitogen=use_mitogen, merge_logs=merge_logs)
        cotea_pb2_grpc.add_CoteaWorkerServicer_to_server(cotea_worker_servicer, self.server)

        addr = "localhost:" + port
        creds = grpc.local_server_credentials()
        self.server.add_secure_port(address=addr, server_credentials=creds)
    
    def start(self):
        print("\tstarting grpc-cotea {} on port {}".format(self.logging_lbl, self.port))
        self.server.start()
        self.server.wait_for_termination()


def start_cotea_worker_server(port, logging_lbl, grpc_server=None, use_mitogen=False, merge_logs=True):
    cotea_srv = CoteaWorkerServer(
        port=port,
        logging_lbl=logging_lbl,
        grpc_server=grpc_server,
        use_mitogen=use_mitogen,
        merge_logs=merge_logs
    )
    cotea_srv.start()
