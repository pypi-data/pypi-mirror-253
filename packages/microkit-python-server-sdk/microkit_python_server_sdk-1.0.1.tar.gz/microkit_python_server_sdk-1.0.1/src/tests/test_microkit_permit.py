import unittest
from microkit_python_server_sdk.microkit import Microkit



class PermissionsTest(unittest.TestCase):

    def test_permit(self):
        service_name = 'permissions_test'
        user = {'email': 'someone@somewhere.com'}
        token = 'd8114911-4f06-4eaf-bc15-59bbc9db4ad7-bQOctxy7zKjZeb9n+M1IBA=='

        # Assuming the microKit and initializeKit methods are present in your module
        microkit = Microkit.initialize_kit(
            token, user, {'base_url': 'localhost', 'http': True, 'port': 8030, 'service': service_name, 'update_rate': 10000}
        )

        email =  microkit.permissions_kit.permit('GET', '/user/profile', 'user')
        uuid =  microkit.permissions_kit.permit('POST', '/articles/create', 'admin', {'ip': '10.0.0.1', 'user': 'chaim'})
        _new =  microkit.permissions_kit.permit('GET', '/articles', 'admin', {'ip': '10.0.0.1', 'user': 'chaim'})

        self.assertFalse(email)
        self.assertTrue(uuid)
        self.assertFalse(_new)

if __name__ == '__main__':
    unittest.main()


# class MicrokitTestCase(unittest.TestCase):
   
#     def test_initializeKit (self):
#         microkit = Microkit.initialize_kit("83578f1b-e460-43ce-a481-a1efd5382496-B+XtrA4P/2nDYHmrh+Ts/g==", {}, {"base_url": "localhost", "port": "8030", "http": True, 'polling_on': False})
            
#         microkit.config_kit.ports.change.subscribe(callback)

    

# if __name__ == '__main__':
#     unittest.main()