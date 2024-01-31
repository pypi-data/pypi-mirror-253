import os
import json

from grpc_cotea.cotea_pb2 import TaskResult
from grpc_cotea.grpc_cotea_exception import GrpcCoteaException


def set_env_vars(env_vars):
    for env_var in env_vars:
        var = env_var.key
        value = env_var.value

        os.environ[var] = value


def unset_env_vars(env_vars):
    for env_var in env_vars:
        var = env_var.key

        if var in os.environ:
            os.environ.pop(var)


def make_dict(list_of_grps_map):
    res = {}

    for m in list_of_grps_map:
        k = m.key
        v = m.value

        res[k] = v
    
    return res


def make_grpc_task_result(task_result, ignr_errs=False, ignr_unrch=False):
    res = TaskResult()

    res.ok = True
    res.task_name = task_result.task_name
    res.is_changed = task_result.is_changed
    res.is_failed = task_result.is_failed
    res.is_skipped = task_result.is_skipped
    res.is_unreachable = task_result.is_unreachable
    res.stderr = task_result.stderr
    res.msg = task_result.msg
    res.results_dict_str = json.dumps(task_result.result)
    res.is_ignored_errors = False
    res.is_ignored_unreachable = False

    if res.is_failed or res.is_unreachable:
        res.ok = False
    
    if ignr_errs:
        res.is_ignored_errors = True
    
    if ignr_unrch:
        res.is_ignored_unreachable = True

    try:
        res.stdout = task_result.stdout
    except Exception as e:
        pass

    return res


def set_ansible_library(new_ans_lib_str):
    cur_ans_lib = ""

    if "ANSIBLE_LIBRARY" in os.environ:
        cur_ans_lib = os.environ["ANSIBLE_LIBRARY"]

    new_ans_lib_values = new_ans_lib_str.split(os.pathsep)

    for new_value in new_ans_lib_values:
        if new_value not in cur_ans_lib:
            cur_ans_lib += new_value + os.pathsep
    
    os.environ["ANSIBLE_LIBRARY"] = cur_ans_lib

    return True, ""


def set_mitogen():
    import grpc_cotea
    grpc_cotea_init_path = grpc_cotea.__file__
    grpc_cotea_init_path_splited = os.path.split(grpc_cotea_init_path)

    error_msg_beg = "Mitogen setting - FAIL. Splited path: {}. "
    error_msg_beg = error_msg_beg.format(grpc_cotea_init_path_splited)
    error_msg_beg += "Error: {}"

    if len(grpc_cotea_init_path_splited) != 2:
        err_msg = "len(os.path.split(grpc_cotea.__file__)) != 2 but should be "
        err_msg += "path to grpc_cotea module + __init__.py."
        error_or_warning = error_msg_beg.format(err_msg)

        return False, error_or_warning
    
    if grpc_cotea_init_path_splited[1] != "__init__.py":
        err_msg = "os.path.split(grpc_cotea.__file__)[1] != __init__.py but should."
        error_or_warning = error_msg_beg.format(err_msg)

        return False, error_or_warning
    
    grpc_cotea_path = grpc_cotea_init_path_splited[0]
    if not os.path.isdir(grpc_cotea_path):
        err_msg = "{} is not dir but should."
        err_msg = err_msg.format(grpc_cotea_path)
        error_or_warning = error_msg_beg.format(err_msg)

        return False, error_or_warning
    
    mitogen_const_path = "ansible_mitogen/plugins/strategy"

    mitogen_path = os.path.join(grpc_cotea_path, mitogen_const_path)
    if not os.path.isdir(mitogen_path):
        err_msg = "{} is not dir but should."
        err_msg = err_msg.format(mitogen_path)
        error_or_warning = error_msg_beg.format(err_msg)
        
        return False, error_or_warning
    
    os.environ["ANSIBLE_STRATEGY_PLUGINS"] = mitogen_path
    os.environ["ANSIBLE_STRATEGY"] = "mitogen_linear"

    return True, ""


def unset_env_vars_list(env_vars_list):
    for env_var in env_vars_list:
        os.environ.pop(env_var)


def get_start_pb_content(args):
    start_pb = '''---
- name: Play
  hosts: {hosts}
  gather_facts: {gather_facts}
  tasks:
  - name: {internal_helping_task_name}
    debug:
      msg: "This is internal helping task that does nothing"
  - name: {internal_helping_task_name}
    debug:
      msg: "This is internal helping task that does nothing"
    '''

    try:
        start_pb = start_pb.format(**args)
    except KeyError as e:
        msg = f"Error during start pb content\
        template vars formating (probably required key is missing): {str(e)}"
        raise GrpcCoteaException(msg)

    return start_pb
    