
from microkit_python_server_sdk.http_client import HttpClient
import json
class Permit():
   def __init__(self, config):
        self.config = config
        self.client = HttpClient.get_instance()
        
   def permit (self, method, path, role, data = {}):
     
      project_id = self.config.get("key_vars_values")["project_id"]
      # , service: config.get('service') || '', data
      res = self.client.post("check_permissions", "permit",{ "project_id": project_id, "method": method, "path": path, "role": role, "data": data, "service": self.config.get('service') or ''})
      res = json.loads(res.decode('utf-8'))
      return res["permit"] or False
    
    

    