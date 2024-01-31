import os
import sys

from multiprocessing.connection import Connection
from grpc_cotea.cotea_worker_spawner import CoteaLocalhostWorkerSpawner
from grpc_cotea.worker_connecter import WorkerData

    
class WorkerMakerBase:
    def __init__(self): pass

    def start(self): pass


class WorkerMakerLocal:
    def __init__(self, conn_with_worker_connecter: Connection, gateway_port="50051", use_mitogen=False,
                 merge_logs=True):
        self.conn = conn_with_worker_connecter
        self.worker_spawner = CoteaLocalhostWorkerSpawner(gateway_port=gateway_port, use_mitogen=use_mitogen, merge_logs=merge_logs)

        self.id_to_worker_obj = {}

    def start(self):
        print("workers maker - start to work")
        while True:
            msg = self.conn.recv()

            if isinstance(msg, str):
                w_id = msg
                w = self.id_to_worker_obj.get(w_id)
                if w is not None:
                    self.worker_spawner.despawn(w)
                    self.id_to_worker_obj.pop(w_id)
            else:
                w = self.worker_spawner.spawn()
                w.start_work()
                
                tmp_w_id = w.get_worker_id()
                tmp_w_addr = w.get_addr()
                
                tmp_wd = WorkerData(
                    id=tmp_w_id,
                    addr=tmp_w_addr
                )

                self.id_to_worker_obj[tmp_w_id] = w

                self.conn.send(tmp_wd)