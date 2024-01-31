import grpc
import grpc_cotea.cotea_pb2 as cotea_pb2
import grpc_cotea.cotea_pb2_grpc as cotea_pb2_grpc
import logging
import threading
import time
import uuid

from grpc_cotea.worker_connecter import WorkerConnecterBase


class CoteaGatewayServicer(cotea_pb2_grpc.CoteaGatewayServicer):
    def __init__(self, workers_connecter:WorkerConnecterBase, initial_worker_count=5, wokers_to_add=2, log_lbl="gateway", log_lvl=logging.INFO,
                gateway_port="50051", workers=None, workers_killing_timeout=300):
        
        logging.basicConfig(format="%(name)s %(asctime)s %(message)s", \
            datefmt="%H:%M:%S", level=log_lvl)
        self.logger = logging.getLogger(log_lbl)
        self.logger.info("cotea GRPC server gateway - start to work")

        self.workers_killing_timeout = workers_killing_timeout

        self.worker_id_to_client_stub = {}
        self.worker_id_to_addr = {}
        self.worker_is_busy = {}
        self.session_id_to_worker_id = {}
        
        self.grpc_worker_channel_options = [('grpc.max_send_message_length', 100 * 1024 * 1024),
        ('grpc.max_receive_message_length', 100 * 1024 * 1024)]
        self.grpc_local_channel_cred = grpc.local_channel_credentials()

        self.lock = threading.Lock()
        self.workers_connecter = workers_connecter

        self._create_n_workers(initial_worker_count)

        self.initial_workers_count = initial_worker_count
        self.cur_workers_count = initial_worker_count
        self.wokers_to_add = wokers_to_add

        self.workers_cleaning_thread = threading.Thread(target=self._clean_unused_workers)
        self.workers_cleaning_thread.start()

        # if workers:
        #     self._embed_workers(workers)
        # else:
        #     self.worker_spawner = CoteaLocalhostWorkerSpawner(gateway_port=gateway_port)
        #     self._create_n_workers(n=initial_worker_count)

        # self.current_workers_count = len(self.workers)
        # self.wokers_to_add = wokers_to_add
    

    def _create_n_workers(self, n):
        self.logger.info("creating {} workers".format(n))
        for _ in range(n):
            self._create_worker()


    def _create_worker(self):
        wd = self.workers_connecter.create_worker()
        self._embed_worker(wd.addr, wd.id)


    def _embed_worker(self, w_addr, w_id):
        creds = self.grpc_local_channel_cred
        options = self.grpc_worker_channel_options
        channel = grpc.secure_channel(w_addr, credentials=creds, options=options)
        stub = cotea_pb2_grpc.CoteaWorkerStub(channel)

        # if not self._check_worker(stub, addr):
        #     self.logger.info("Failed to create worker at {}".format(addr))
        #     return

        self.worker_id_to_client_stub[w_id] = stub
        self.worker_id_to_addr[w_id] = w_addr
        self.worker_is_busy[w_id] = False


    def _find_free_worker(self):
        free_worker = False
        worker_id = None

        for w_id in self.worker_is_busy:
            if not self.worker_is_busy[w_id]:
                free_worker = True
                worker_id = w_id
        
        return free_worker, worker_id
    
    
    def _check_worker(self, stub, addr):
        check_attempts = 0
        max_check_attempts = 10
        check_complite = False

        check_attempts += 1

        while check_attempts <= max_check_attempts:
            try:
                hc = stub.HealthCheck(cotea_pb2.EmptyMsg())
                if hc.ok:
                    check_complite = True
            except Exception as e:
                msg = "Attemt#{} to connect to worker at {} - FAIL"
                self.logger.info(msg.format(check_attempts, addr))
                self.logger.debug("The exception was: {}".format(str(e)))
            
            if check_complite:
                msg = "Attemt#{} to connect to worker at {} - OK"
                self.logger.info(msg.format(check_attempts, addr))
                break
            
            check_attempts += 1
            time.sleep(0.01)
        
        if check_complite:
            return True
        
        return False


    def _clean_unused_workers(self):
        while True:
            time.sleep(self.workers_killing_timeout)
            clean_msg = None

            extra_workers_count = self.cur_workers_count - self.initial_workers_count
            
            if extra_workers_count > 0:
                self.lock.acquire()

                free_workers_ids = []
                free_workers_count = 0

                for w_id in self.worker_is_busy:
                    if not self.worker_is_busy[w_id]:
                        free_workers_ids.append(w_id)
                        free_workers_count += 1

                if free_workers_count > 0:
                    workers_to_kill_count = 0

                    if extra_workers_count >= free_workers_count:
                        workers_to_kill_count = free_workers_count
                    else:
                        workers_to_kill_count = extra_workers_count
                    
                    clean_msg = "{} workers with pids {} were sentenced to die".format(workers_to_kill_count, \
                                            free_workers_ids[:workers_to_kill_count])
                    self.logger.info(clean_msg)

                    for i in range(workers_to_kill_count):
                        killing_worker_id = free_workers_ids[i]

                        if killing_worker_id in self.worker_id_to_client_stub:
                            self.worker_id_to_client_stub.pop(killing_worker_id)
                        
                        if killing_worker_id in self.worker_id_to_addr:
                            self.worker_id_to_addr.pop(killing_worker_id)
                        
                        if killing_worker_id in self.worker_is_busy:
                            self.worker_is_busy.pop(killing_worker_id)

                        self.cur_workers_count -= 1
                        self.workers_connecter.delete_worker(killing_worker_id)
                
                self.lock.release()


    def StartSession(self, request, context):
        self.logger.info("StartSession procedure called")

        self.lock.acquire()

        free_worker, worker_id = self._find_free_worker()

        self.logger.debug("Free worker search: {}, {}".format(free_worker, worker_id))

        if not free_worker:
            self._create_n_workers(n=self.wokers_to_add)

            self.cur_workers_count += self.wokers_to_add

            time.sleep(0.25)
            
            # TODO: more checks
            _, worker_id = self._find_free_worker()

            self.logger.info("Free worker search: {}, {}".format(free_worker, worker_id))
        
        new_session_id = str(uuid.uuid1())
        self.worker_is_busy[worker_id] = True
        self.session_id_to_worker_id[new_session_id] = worker_id

        self.lock.release()

        stub = None
        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id)

            return cotea_pb2.StartSessionMSG(ok=False, error_msg=err_msg)
        
        start_res = stub.StartSession(cotea_pb2.SessionID(session_ID=new_session_id))
        if not start_res.ok:
            err_msg = "Worker's {} StartSession() during session {} returned error: {}"
            err_msg = err_msg.format(worker_id, new_session_id, start_res.error_msg)

            return cotea_pb2.StartSessionMSG(ok=False, error_msg=err_msg)
 
        return cotea_pb2.StartSessionMSG(ok=True, ID=new_session_id, error_msg="")
        

    def InitExecution(self, request, context):
        self.logger.info("InitExecution procedure called")

        s_id = request.session_ID
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        conf = cotea_pb2.WorkerConfig(
            session_ID=request.session_ID,
            hosts=request.hosts,
            not_gather_facts=request.not_gather_facts,
            inv_str = request.inv_str,
            extra_vars_str=request.extra_vars_str,
            env_vars=list(request.env_vars),
            ansible_library=request.ansible_library
        )

        addr = self.worker_id_to_addr[worker_id]
        if not self._check_worker(stub, addr):
            msg = "Failed to connect to session's worker at {}"
            self.logger.info(msg.format(addr))

            return cotea_pb2.Status(ok=False, error_msg=msg)

        init_res = stub.InitExecution(conf)
        if not init_res.ok:
            self._close_session(s_id)

        return init_res
    

    def RunTask(self, request, context):
        #self._print_thread_info("RunTask")
        self.logger.info("RunTask procedure called")

        s_id = request.session_ID
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.TaskResults(
                task_adding_ok=False,
                task_adding_error=err_msg
            )

            return res

        task = cotea_pb2.WorkerTask(
            task_str=str(request.task_str),
            is_dict=request.is_dict
        )

        addr = self.worker_id_to_addr[worker_id]
        if not self._check_worker(stub, addr):
            msg = "Failed to connect to session's worker at {}"
            self.logger.info(msg.format(addr))

            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=msg)

        return stub.RunTask(task)


    def StopExecution(self, request, context):
        #self._print_thread_info("StopExecution")
        self.logger.info("StopExecution procedure called")

        s_id = request.session_ID
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        addr = self.worker_id_to_addr[worker_id]
        if not self._check_worker(stub, addr):
            msg = "Failed to connect to session's worker at {}"
            self.logger.info(msg.format(addr))

            return cotea_pb2.Status(ok=False, error_msg=msg)

        stop_execution_res = stub.StopExecution(cotea_pb2.EmptyMsg())
        
        return stop_execution_res


    def GetVar(self, request, context):
        var_name = request.var_name
        log_msg = "GetVar procedure called - requested var is {}"
        log_msg = log_msg.format(var_name)

        self.logger.info(log_msg)

        s_id = request.session_ID
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        addr = self.worker_id_to_addr[worker_id]
        if not self._check_worker(stub, addr):
            err_msg = "Failed to connect to session's worker at {}"
            self.logger.info(msg.format(addr))

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        ansible_var_msg_to_worker = cotea_pb2.AnsibleVarMsg(
            var_name=request.var_name
        )
        
        return stub.GetVar(ansible_var_msg_to_worker)


    def GetStats(self, request, context):
        #self._print_thread_info("StopExecution")
        self.logger.info("GetStats procedure called")

        s_id = request.session_ID
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.String(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        addr = self.worker_id_to_addr[worker_id]
        if not self._check_worker(stub, addr):
            err_msg = "Failed to connect to session's worker at {}"
            self.logger.info(msg.format(addr))

            res = cotea_pb2.String(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        return stub.GetStats(cotea_pb2.EmptyMsg())


    def CloseSession(self, request, context):
        self.logger.info("CloseSession procedure called")

        return self._close_session(request.session_ID)

        
    def _close_session(self, s_id):
        worker_id = None
        stub = None

        if s_id in self.session_id_to_worker_id:
            worker_id = self.session_id_to_worker_id[s_id]
        else:
            err_msg = "No session with ID {}".format(s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res
        
        if worker_id in self.worker_id_to_client_stub:
            stub = self.worker_id_to_client_stub[worker_id]
        else:
            err_msg = "Worker ID {} of session {} was not in worker_id_to_client_stub dict but should"
            err_msg = err_msg.format(worker_id, s_id)

            res = cotea_pb2.Status(
                ok=False,
                error_msg=err_msg
            )

            return res

        self.lock.acquire()
        self.worker_is_busy[worker_id] = False
        self.session_id_to_worker_id.pop(s_id)
        self.lock.release()

        return stub.CloseSession(cotea_pb2.EmptyMsg())