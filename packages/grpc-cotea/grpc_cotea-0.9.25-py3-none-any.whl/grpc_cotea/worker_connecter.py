import time

from multiprocessing.connection import Connection


class WorkerData:
    def __init__(self, id, addr):
        self.id = id
        self.addr = addr


class WorkerConnecterBase:
    '''
    This is base class for the interaction with workers
    '''

    def __init__(self): pass

    def create_worker(self) -> WorkerData: pass

    def delete_worker(self, w_id): pass


class WorkerConnectorLocal(WorkerConnecterBase):
    def __init__(self, conn_with_worker_maker: Connection):
        super().__init__()

        self.conn = conn_with_worker_maker
    
    def create_worker(self) -> WorkerData:
        self.conn.send(None)
        
        wd = self.conn.recv()

        # TODO: check
        # if not isinstance(wd, WorkerData):

        return wd
    
    def delete_worker(self, w_id):
        send_res = self.conn.send(w_id)
        