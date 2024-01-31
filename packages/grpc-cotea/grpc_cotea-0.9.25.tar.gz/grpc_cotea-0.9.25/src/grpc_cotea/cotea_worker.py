import grpc_cotea.utils
import grpc_cotea.cotea_pb2 as cotea_pb2
import grpc_cotea.cotea_pb2_grpc as cotea_pb2_grpc
import threading
import logging
import uuid
import os
import json
import shutil
import tempfile
import sys
import importlib.resources as pkg_res

from jinja2 import Environment, FileSystemLoader
from grpc_cotea.ansible_execution_config import ansible_exec_config
from grpc_cotea.grpc_cotea_exception import GrpcCoteaException


class CoteaWorkerServicer(cotea_pb2_grpc.CoteaWorkerServicer):
    def __init__(self, logging_lbl="worker", logging_lvl=logging.INFO, use_mitogen=False, merge_logs=True):
        # todo: make some constants place
        self.workers_logs_dir_path = "/tmp/gc_workers_logs"
        self.workers_contexts_dir_path = "/tmp/gc_workers_contexts"
        
        try:
            os.mkdir(self.workers_logs_dir_path)
        except FileExistsError: # other worker has already created
            pass

        try:
            os.mkdir(self.workers_contexts_dir_path)
        except FileExistsError: # other worker has already created
            pass
        
        self.merge_logs = merge_logs
        self.logging_lbl = logging_lbl
        self.logging_lvl = logging_lvl
        self.logger = None
        self._redirect_logging_to_stdout()
        
        self.session_logs_file_path = None
        self.session_logs_file = None

        self.arg_maker = None
        self.ansible_runner = None
        self.vars_set = None
        self.executions = 0
        self.executed_tasks_count = 0
        self.env_vars_were_set = []
        self.use_mitogen = use_mitogen

        #self.pb_template_file_name = "start_tmpl.j2"
        #self.pb_start_template = None
        #self._create_template()
        self.session_context_dir_path = None
        self.cur_session_id = None
        
        self.pb_start_yaml_file_name = None

        self.internal_helping_task_name = "Internal-Empty-Task"

        self.internal_helping_task_str = "  - name: {}\n"
        self.internal_helping_task_str += "    debug:\n"
        self.internal_helping_task_str += '      msg: "This is internal helping task that does nothing"\n'
        self.internal_helping_task_str = self.internal_helping_task_str.format(self.internal_helping_task_name)


    def StartSession(self, request, context):
        self.logger.info("StartSession procedure called")

        self.cur_session_id = request.session_ID
        
        self.session_logs_file_path = os.path.join(self.workers_logs_dir_path, self.cur_session_id) + ".log"
        self.session_logs_file = open(self.session_logs_file_path, "a")

        redirection_msg = ""
        
        if self.merge_logs:
            redirection_msg = "{}'s all stdout and stderr will be redirected to {}"
        else:
            redirection_msg = "{}'s Ansible stdout only and stderr will be redirected to {}"
        redirection_msg = redirection_msg.format(self.logging_lbl, self.session_logs_file_path)
        self.logger.info(redirection_msg)
        
        if self.merge_logs:
            self._redirect_logging_to_file(self.session_logs_file_path)

        sys.stdout = self.session_logs_file
        sys.stderr = self.session_logs_file

        # creating session context dir
        self.session_context_dir_path = os.path.join(self.workers_contexts_dir_path, self.cur_session_id + "_context")

        try:
            os.mkdir(self.session_context_dir_path)
        except FileExistsError as e:
            msg = "During creating session {} context dir got exception: {}\nSkipping"
            msg = msg.format(self.cur_session_id, str(e))
            self.logger.info(msg)
            
        return cotea_pb2.Status(ok=True)
        

    def InitExecution(self, request, context):
        #self._print_thread_info("InitExecution")
        self.logger.info("InitExecution procedure called")

        if self.cur_session_id is None or self.session_context_dir_path is None:
            err_msg = "It seems like StartSession() wasn't called, call it first"

            return cotea_pb2.Status(ok=False, error_msg=err_msg)
        
        got_session_ID = request.session_ID
        if got_session_ID != self.cur_session_id:
            err_msg = "InitExecution got session with ID {}, but worker's current session ID is {}. "
            err_msg = err_msg.format(got_session_ID, self.cur_session_id)

            return cotea_pb2.Status(ok=False, error_msg=err_msg)

        if self.ansible_runner != None:
            try:
                self._finish_execution()
            except Exception as e:
                err_msg = "Durring cotea.runner finishing after previous run"
                err_msg += " an exception has occurred - {}"
                err_msg = err_msg.format(str(e))
                self.logger.info(err_msg)

                return cotea_pb2.Status(ok=False, error_msg=err_msg)
   
        ansible_exec_conf = ansible_exec_config(request)

        hosts = request.hosts
        gathering_facts_str = "true"
        not_gather_facts = request.not_gather_facts
        if not_gather_facts:
            gathering_facts_str = "false"
        
        template_data = {"hosts": hosts,
                         "internal_helping_task_name": self.internal_helping_task_name,
                         "gather_facts": gathering_facts_str}
        try:
            start_pb_content = grpc_cotea.utils.get_start_pb_content(template_data)
        except GrpcCoteaException as e:
            err_msg = str(e)
            self.logger.info(err_msg)

            return cotea_pb2.Status(ok=False, error_msg=err_msg)
                
        pb_path = os.path.join(self.session_context_dir_path, "start-" + self.cur_session_id + ".yaml")
        self.pb_start_yaml_file_name = pb_path

        pb_path_file = open(pb_path, "w")
        pb_path_file.write(start_pb_content)
        pb_path_file.close()

        inv_str = request.inv_str
        extra_vars_str = request.extra_vars_str
        env_vars = request.env_vars
        ansible_library = request.ansible_library

        ansible_exec_conf.pretty_print()
        
        if self.vars_set:
            grpc_cotea.utils.unset_env_vars(self.vars_set)
        
        grpc_cotea.utils.set_env_vars(env_vars)
        self.vars_set = env_vars

        if ansible_library != "":
            setting_ok, err_msg = grpc_cotea.utils.set_ansible_library(ansible_library)
            if not setting_ok:
                err_msg = "ANSIBLE_LIBRARY setting error: " + err_msg
                return cotea_pb2.Status(ok=False, error_msg=err_msg)
            
            check_msg = "ANSIBLE_LIBRARY value check: " + os.environ.get("ANSIBLE_LIBRARY")
            self.logger.info(check_msg)

            self.env_vars_were_set.append("ANSIBLE_LIBRARY")
        
        if self.use_mitogen:
            mitogen_set_ok, err_msg = grpc_cotea.utils.set_mitogen()
            if not mitogen_set_ok:
                self.logger.info(err_msg)
                self.logger.info("As a result, worker will work without mitogen")
            else:
                self.logger.info("Mitogen setting - OK")
                
                self.env_vars_were_set.append("ANSIBLE_STRATEGY_PLUGINS")
                self.env_vars_were_set.append("ANSIBLE_STRATEGY")

        from cotea.utils import remove_modules_from_imported

        # the imports below should invoke because it cleanes
        # previous execution context
        remove_modules_from_imported(module_name_like="cotea")

        from cotea.runner import runner
        from cotea.arguments_maker import argument_maker
        # import logging
        
        self.arg_maker = argument_maker()

        if inv_str != "":
            tmp_inv_file_path = os.path.join(self.session_context_dir_path, "inv")

            with open(tmp_inv_file_path, "w") as tmp_inv:
                tmp_inv.write(inv_str)

            self.arg_maker.add_arg("-i", tmp_inv_file_path)
        #self.arg_maker.add_arg("-vvv")
        
        if len(extra_vars_str) > 0:
            self.arg_maker.add_arg("--extra-vars", extra_vars_str)

        try:
            self.ansible_runner = runner(pb_path, self.arg_maker) #, show_progress_bar=True, debug_mod=logging.DEBUG)
            special_task_found = False

            while self.ansible_runner.has_next_play():
                while self.ansible_runner.has_next_task():
                    next_task_name = self.ansible_runner.get_next_task_name()
                    self.ansible_runner.run_next_task()

                    if next_task_name == self.internal_helping_task_name:
                        special_task_found = True
                        break
                
                if special_task_found:
                    break
            
            if self.ansible_runner.was_error():
                err_msg = self.ansible_runner.get_error_msg()
                self._finish_execution()
                return cotea_pb2.Status(ok=False, error_msg=err_msg)

            if not special_task_found:
                err_msg = "Special task with name {} was not found".format(self.internal_helping_task_name)
                self._finish_execution()
                return cotea_pb2.Status(ok=False, error_msg=err_msg)

        except Exception as e:
            err_msg = "Durring cotea.runner creating and starting"
            err_msg += " an exception has occurred - {}"
            err_msg = err_msg.format(str(e))
            self.logger.info(err_msg)

            return cotea_pb2.Status(ok=False, error_msg=err_msg)
        
        self.executions += 1

        return cotea_pb2.Status(ok=True)
    

    def RunTask(self, request, context):
        task_str = request.task_str

        #self._print_thread_info("RunTask")
        self.logger.info("RunTask procedure called, got task:\n{}".format(task_str))

        if self.ansible_runner == None:
            error_msg = "Ansible execution was not inited. " 
            error_msg += "You should call InitExecution() first."

            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)

        is_dict = request.is_dict

        try:
            adding_ok, error_msg = self.ansible_runner.add_new_task(task_str, is_dict)
            if not adding_ok:
                return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)
            
            new_task_obj = self.ansible_runner.get_new_added_task()
        except Exception as e:
            error_msg = "Internal Ansible error during the execution:\n" 
            error_msg += str(e)

            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)

        ignr_errs = False
        ignr_unrch = False

        if hasattr(new_task_obj, "ignore_errors"):
            if new_task_obj.ignore_errors:
                ignr_errs = True
        
        if hasattr(new_task_obj, "ignore_unreachable"):
            if new_task_obj.ignore_unreachable:
                ignr_unrch = True
        
        try:
            self.ansible_runner.ignore_errors_of_next_task()
            self.ansible_runner.dont_add_last_task_after_new()

            executed_tasks_count = 0
            task_results = []
            some_task_failed = False

            while self.ansible_runner.has_next_task():
                next_task_name = self.ansible_runner.get_next_task_name()
                task_result = self.ansible_runner.run_next_task()

                executed_tasks_count += 1

                if next_task_name == self.internal_helping_task_name:
                    executed_tasks_count -= 1
                    break
                else:
                    task_results.extend(task_result)
                
                for task in task_result:
                    if task.is_failed or task.is_unreachable:
                        some_task_failed = True
                        break
                
                if some_task_failed:
                    # if that was some an include, we should skip 
                    # tasks that are left after the failed one 
                    while True:
                        skipped_task_name = self.ansible_runner.skip_next_task()
                        if skipped_task_name == self.internal_helping_task_name or skipped_task_name == "":
                            break
                    
                    # this could be dangerous
                    # additional loop stop condition is needed

                    break
                
                self.ansible_runner.ignore_errors_of_next_task()
                self.ansible_runner.dont_add_last_task_after_new()
                
        except Exception as e:
            error_msg = "Internal Ansible error during the execution:\n" 
            error_msg += str(e)

            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)
        
        self.executed_tasks_count += executed_tasks_count

        if executed_tasks_count == 0:
            error_msg = "Has no tasks but should. Probably the include task failed."

            try:
                self._finish_execution()
            except Exception as e:
                err_msg = "Durring cotea.runner finishing after"
                err_msg += " an exception has occurred - {}"
                err_msg = err_msg.format(str(e))
                self.logger.info(err_msg)

                error_msg += "\nAlso " + err_msg


            self.logger.debug(error_msg)
            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)

        try:
            adding_ok, error_msg = self.ansible_runner.add_new_task(self.internal_helping_task_str)
        except Exception as e:
            error_msg = "Internal Ansible error during the execution:\n" 
            error_msg += str(e)

            return cotea_pb2.TaskResults(task_adding_ok=False, task_adding_error=error_msg)

        grpc_task_results = []

        for task_result in task_results:
            grpc_task_res = grpc_cotea.utils.make_grpc_task_result(task_result, ignr_errs, ignr_unrch)
            grpc_task_results.append(grpc_task_res)

        return cotea_pb2.TaskResults(task_adding_ok=True, task_results=grpc_task_results)


    def StopExecution(self, request, context):
        #self._print_thread_info("StopExecution")
        self.logger.info("StopExecution procedure called")

        try:
            self._finish_execution()
        except Exception as e:
            err_msg = "Durring cotea.runner finishing"
            err_msg += " an exception has occurred - {}"
            err_msg = err_msg.format(str(e))
            self.logger.info(err_msg)

            return cotea_pb2.Status(ok=False, error_msg=err_msg)
        
        return cotea_pb2.Status(ok=True)


    def GetVar(self, request, context):
        var_name = request.var_name
        log_msg = "GetVar procedure called - requested var is {}"
        log_msg = log_msg.format(var_name)

        self.logger.info(log_msg)

        if self.ansible_runner == None:
            err_msg = "Ansible execution was not inited. " 
            err_msg += "You should call InitExecution() first."

            return cotea_pb2.AnsibleVar(ok=False, error_msg=err_msg)
        
        var_name = request.var_name
        var_value = ""

        try:
            var_value = self.ansible_runner.get_variable(var_name)
        except Exception as e:
            err_msg = "Exception occurred during "
            err_msg += "cotea.runner.get_variable method call: "
            err_msg += str(e)

            return cotea_pb2.AnsibleVar(ok=False, name=var_name, error_msg=err_msg)
        
        if isinstance(var_value, dict):
            var_value = json.dumps(var_value)
        else:
            var_value = str(var_value)

        res = cotea_pb2.AnsibleVar(
                ok=True,
                name=var_name,
                value=var_value
        )

        log_msg = "GetVar procedure result:\n{} = {}\n"
        log_msg = log_msg.format(var_name, var_value)

        self.logger.info(log_msg)

        return res


    def GetStats(self, request, context):
        log_msg = "GetStats procedure called"

        self.logger.info(log_msg)

        if self.ansible_runner == None:
            err_msg = "Ansible execution was not inited. " 
            err_msg += "You should call InitExecution() first."

            return cotea_pb2.String(ok=False, error_msg=err_msg)
        
        stats = None
        stats_str = ""

        try:
            stats = self.ansible_runner.get_stats()
        except Exception as e:
            err_msg = "Exception occurred during "
            err_msg += "cotea.runner.get_variable method call: "
            err_msg += str(e)

            return cotea_pb2.String(ok=False, error_msg=err_msg)
        
        if isinstance(stats, dict):
            stats_str = json.dumps(stats)
        else:
            stats_str = str(stats)

        res = cotea_pb2.String(
                ok=True,
                res=stats_str
        )

        log_msg = "GetStats procedure result:\n{}\n"
        log_msg = log_msg.format(stats_str)

        self.logger.info(log_msg)

        return res


    def CloseSession(self, request, context):
        self.logger.info("CloseSession procedure called")

        try:
            shutil.rmtree(self.session_context_dir_path)
        except OSError as e:
            msg = "Session context dir {} can't be removed because of: {}"
            msg = msg.format(self.session_context_dir_path, str(e))
            self.logger.info(msg)
        
        self.session_context_dir_path = None
        self.cur_session_id = None

        # In a case one calls directly CloseSession
        # without calling StopExecution first
        # (one should not do that)
        try:
            self._finish_execution()
        except Exception as e:
            err_msg = "Durring cotea.runner finishing"
            err_msg += " an exception has occurred - {}"
            err_msg = err_msg.format(str(e))
            self.logger.info(err_msg)

            return cotea_pb2.Status(ok=False, error_msg=err_msg)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        if self.merge_logs:
            self._redirect_logging_to_stdout()
        self.session_logs_file.close()
        
        return cotea_pb2.Status(ok=True)


    def HealthCheck(self, request, context):
        #self._print_thread_info("HealthCheck")
        self.logger.info("HealthCheck procedure called")

        hs = cotea_pb2.WorkerHealthStatus(
            ok=True,
            executions_count=self.executions,
            executed_tasks_count=self.executed_tasks_count
        )
        
        return hs
    

    def _finish_execution(self):
        if self.ansible_runner:
            self.ansible_runner.finish_ansible()
        
        self.ansible_runner = None

        grpc_cotea.utils.unset_env_vars_list(self.env_vars_were_set)
        self.env_vars_were_set = []


    def _print_thread_info(self, rpc_method_name):
        cur_thread_ID = threading.current_thread().ident
        print("{} - Current thread ID = {}".format(rpc_method_name, cur_thread_ID))
        print("Threads active count =", threading.active_count())
        print(threading.enumerate())


    def _print_var(self, var_name):
        if self.ansible_runner:
            test_var = self.ansible_runner.get_variable(var_name)
            self.logger.info("{} = {}".format(var_name, test_var))
    

    def _create_template(self):
        t_content = pkg_res.read_text("grpc_cotea", self.pb_template_file_name)

        with open(self.pb_template_file_name, "w") as t_file:
            t_file.write(t_content)
        
        templ_env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
        self.pb_start_template = templ_env.get_template(self.pb_template_file_name)


    def _redirect_logging_to_file(self, file_name):
        if "logging" in sys.modules: 
            sys.modules.pop("logging")
        import logging

        logging.basicConfig(filename=file_name, filemode="a", \
                format="%(name)s %(asctime)s %(message)s", \
            datefmt="%H:%M:%S", level=self.logging_lvl)
        
        self.logger = logging.getLogger(self.logging_lbl)


    def _redirect_logging_to_stdout(self):
        if "logging" in sys.modules: 
            sys.modules.pop("logging")
        import logging

        logging.basicConfig(format="%(name)s %(asctime)s %(message)s", \
            datefmt="%H:%M:%S", level=self.logging_lvl)
        
        self.logger = logging.getLogger(self.logging_lbl)