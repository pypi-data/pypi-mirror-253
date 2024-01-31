from multiprocessing import Process
from grpc_cotea.cotea_worker_server import start_cotea_worker_server


class CoteaLocalhostWorker:
    def __init__(self, port, logging_lbl, grpc_server=None, use_mitogen=False, merge_logs=True):
        self.port = port
        self.logging_lbl = logging_lbl
        self.worker_process = Process(target=start_cotea_worker_server, args=(port, logging_lbl, grpc_server, use_mitogen, merge_logs, ))
    

    def get_addr(self):
        return "localhost:" + self.port
    

    def start_work(self):
        self.worker_process.start()
        msg = "{}, pid - {}".format(self.logging_lbl, self.worker_process.pid)
        print(msg)
    
    
    def finish_work(self):
        pid_of_killing = self.worker_process.pid
        base_msg = "Killing {} with pid {}".format(self.logging_lbl, pid_of_killing)
        print(base_msg + "...")

        self.worker_process.kill()
        self.worker_process.join(3)

        exitcode = self.worker_process.exitcode
        if exitcode is None:
            msg = "{} - failed to join process during killing despite SIGKILL was sended"
            msg = msg.format(base_msg)
            print(msg)
        else:
            try:
                self.worker_process.close()
                msg = "{} - success".format(base_msg)
                print(msg)
            except ValueError as e:
                msg = "{} - failed.\nProcess.close() was failed despite join was successful".format(base_msg)
                msg += "\nThe exception was:\n{}".format(str(e))
                print(msg)


    def get_worker_id(self):
        return str(self.worker_process.pid)


class CoteaLocalhostWorkerSpawner:
    def __init__(self, grpc_server=None, gateway_port="50051", use_mitogen=False, merge_logs=True):
        self.gateway_port = int(gateway_port)
        self.current_port = self.gateway_port + 1
        self.grpc_server = grpc_server
        self.use_mitogen = use_mitogen
        self.merge_logs = merge_logs
    

    def spawn(self):
        worker_num = self.current_port - self.gateway_port
        worker_lbl = "worker" + str(worker_num)

        w = CoteaLocalhostWorker(
                str(self.current_port),
                logging_lbl=worker_lbl,
                grpc_server=self.grpc_server,
                use_mitogen=self.use_mitogen,
                merge_logs=self.merge_logs
        )
        self.current_port += 1

        return w
    

    def despawn(self, w: CoteaLocalhostWorker):
        w.finish_work()
        self.current_port -= 1
