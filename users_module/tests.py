from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class UserTest(APITestCase):
    def self(self):
        self.client: APIClient = APIClient()
        # self.register_url = '/auth/users/'
        # self.login_url = '/auth/jwt/create/'

    def test_users_can_register(self):
        data = {
            'email': 'name@gmail.com',
            'password': 'Password12,',
            'username': 'username'
        }
        registration_response = self.client.post('/auth/users', data, 'json')
        self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(registration_response.data('isVerified'))
        print(registration_response)
