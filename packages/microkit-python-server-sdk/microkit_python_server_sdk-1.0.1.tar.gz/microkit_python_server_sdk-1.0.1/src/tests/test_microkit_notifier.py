import unittest
from microkit_python_server_sdk.microkit import Microkit



class NotificationsTest(unittest.TestCase):

    def test_permit(self):
        service_name = 'testing'
        user = {'email': 'someone@somewhere.com'}
        token = '7fa8f128-19fc-41eb-ba9a-70a8f2f16fb7-af6TjQChLMl14kXzzY3MwQ=='

        # Assuming the microKit and initializeKit methods are present in your module
        microkit = Microkit.initialize_kit(
            token, user, {'base_url': 'localhost', 'http': True, 'port': 8030, 'service': service_name, 'update_rate': 10000}
        )

         
        name = 'Test Notifier'
        message_interfaces = [
            {'interface': 'slack', 'template': 'text'},
            # {'interface': 'email', 'template': 'notifier_email'}
        ]
        contacts = ['admins']
        params = {'sender': 'Microkit Notifier'}
        

        email =  microkit.notifications_kit.notify(name=name, message_interfaces=message_interfaces, contacts=contacts, params=params)
       
        self.assertFalse(email)
        

if __name__ == '__main__':
    unittest.main()


# class MicrokitTestCase(unittest.TestCase):
   
#     def test_initializeKit (self):
#         microkit = Microkit.initialize_kit("83578f1b-e460-43ce-a481-a1efd5382496-B+XtrA4P/2nDYHmrh+Ts/g==", {}, {"base_url": "localhost", "port": "8030", "http": True, 'polling_on': False})
            
#         microkit.config_kit.ports.change.subscribe(callback)

    

# if __name__ == '__main__':
#     unittest.main()