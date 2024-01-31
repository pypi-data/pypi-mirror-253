import json


class ansible_exec_config:
    def __init__(self, grpc_request):
        self.session_ID = self._get_attr(grpc_request, "session_ID")
        self.hosts = self._get_attr(grpc_request, "hosts")
        self.inv_str = self._get_attr(grpc_request, "inv_str")
        self.ansible_library = self._get_attr(grpc_request, "ansible_library")
        self.not_gather_facts = self._get_attr(grpc_request, "not_gather_facts")
        
        self.extra_vars = {}
        extra_vars_str = self._get_attr(grpc_request, "extra_vars_str")
        if extra_vars_str is not None:
            try:
                self.extra_vars = eval(extra_vars_str)
            except Exception as e:
                self.extra_vars["error_msg"] = "extra vars string decoding with eval was failed"
                self.extra_vars["string_tried_to_decode"] = extra_vars_str
                self.extra_vars["exception"] = str(e)

        self.env_vars = {}
        env_vars_grpc = self._get_attr(grpc_request, "env_vars")
        if env_vars_grpc is not None:
            for env_var in env_vars_grpc:
                var = env_var.key
                value = env_var.value

                self.env_vars[var] = value
    
    def _get_attr(self, obj, attr_name):
        value = None

        try:
            value = getattr(obj, attr_name)
        except AttributeError:
            pass

        return value
    
    def pretty_print(self):
        printing_str = "----------------------------Ansible execution config----------------------------\n"
        printing_str += "session_ID: {}\n\n".format(self.session_ID)
        printing_str += "hosts: {}\n\n".format(self.hosts)
        printing_str += "inv_str:\n{}\n\n".format(self.inv_str)
        printing_str += "ansible_library: {}\n\n".format(self.ansible_library)
        printing_str += "not_gather_facts: {}\n\n".format(self.not_gather_facts)

        extra_vars_str_to_print = json.dumps(self.extra_vars, sort_keys=True, indent=4, separators=(',', ': '))
        printing_str += "extra_vars:\n{}\n\n".format(extra_vars_str_to_print)

        env_vars_str_to_print = json.dumps(self.env_vars, sort_keys=True, indent=4, separators=(',', ': '))
        printing_str += "env_vars:\n{}\n".format(env_vars_str_to_print)

        printing_str += "--------------------------------------------------------------------------------\n\n"

        print(printing_str)