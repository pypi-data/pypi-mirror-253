from microkit_python_server_sdk.http_client import HttpClient
import json

class Notifications:

    def __init__(self, config):
        self.config = config
        self.client = HttpClient.get_instance()

    def notify(self, name, message_interfaces, contacts, params=None):
        if params is None:
            params = {}

        if not message_interfaces or not isinstance(message_interfaces, list):
            raise ValueError('message_interfaces must be an array with at least one interface')

        if not contacts or not isinstance(contacts, list):
            raise ValueError('contacts must be an array with at least one contact')

        for message_interface in message_interfaces:
            if 'interface' not in message_interface or 'template' not in message_interface:
                raise ValueError('message_interfaces must be an array of objects with interface and template keys')

        if not isinstance(params, dict):
            raise ValueError('params must be an object')

        if not name:
            raise ValueError('Name is required. The name is used to identify the notification in the logs')

        key_vars_values = self.config.get('key_vars_values')
        project_id = key_vars_values['project_id']
        environment_id = key_vars_values['environment_id']

        res = self.client.post("send_notifications", "notify" ,{"project_id": project_id, "environment_id" : environment_id,"name": name, "message_interfaces": message_interfaces, "contacts": contacts, "params": params})
        res = json.loads(res.decode('utf-8'))
        return res["permit"] or False
