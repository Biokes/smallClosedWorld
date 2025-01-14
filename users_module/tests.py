from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from users_module.models import User


class UserTest(APITestCase):
    def self(self):
        self.client: APIClient = APIClient()
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
        }
        self.user = User.objects.create_user(**self.valid_data)
        self.url = '/api/users/'

    def test_users_can_register(self):
        data = {
            'email': 'name@gmail.com',
            'password': 'Password12,',
            'username': 'username'
        }
        registration_response = self.client.post('/auth/users', data, 'json')
        self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(registration_response.data['isVerified'])
        self.assertIn('date_joined', registration_response.data)
        print(registration_response)

    def test_user_can_update_profile(self):
        data = {
            'email': 'name@gmail.com',
            'password': '      ',
            'username': 'username'
        }
        registration_response = self.client.post('/auth/users', data, 'json')
        self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)
        registration_response = self.client.post('/auth/users', data, 'json')
        self.assertEqual(registration_response.status_code, status.HTTP_400_BAD_REQUEST)
        data['email'] = 'name1@gmail.com'
        self.assertEqual(registration_response.status_code, status.HTTP_400_BAD_REQUEST)
        data['password']= 'name1@gmail.67'
        self.assertEqual(registration_response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_create_user_success(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_create_user_missing_field(self):
        data = {
            'username': 'newuser'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)

    def test_create_user_invalid_email(self):
        data = {
            'username': 'newuser',
            'email': 'invalidemail',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_create_user_password_too_short(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': '123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_get_user_details_authenticated(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        response = self.client.get(f'{self.url}{self.user.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_get_user_details_unauthenticated(self):
        response = self.client.get(f'{self.url}{self.user.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user_success(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        update_data = {'email': 'newemail@example.com'}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'newemail@example.com')

    def test_delete_user_success(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        response = self.client.delete(f'{self.url}{self.user.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_user_invalid_field(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        update_data = {'username': ''}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_server_error(self):
        response = self.client.get(f'{self.url}nonexistent/', format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_edge_case_username_length(self):
        long_username = 'a' * 255
        data = {
            'username': long_username,
            'email': 'longusername@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], long_username)

    def test_edge_case_empty_request(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)

    def test_create_user_username_max_length(self):
        max_length_username = 'a' * 150
        data = {
            'username': max_length_username,
            'email': 'maxusername@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_username_empty(self):
        data = {
            'username': '',
            'email': 'emptyusername@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_create_user_duplicate_username(self):
        data = {
            'username': 'testuser',
            'email': 'duplicate@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_create_user_email_already_exists(self):
        data = {
            'username': 'newuser',
            'email': self.user.email,
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_edge_case_password_length(self):
        long_password = 'a' * 255
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': long_password
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_patch_request(self):
        update_data = {'nonexistent_field': 'test'}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_nonexistent_field(self):
        update_data = {'nonexistent_field': 'value'}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_special_characters_username(self):
        data = {
            'username': '@user#',
            'email': 'specialchar@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_special_characters_email(self):
        data = {
            'username': 'user1',
            'email': 'user!@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user_invalid_email(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        update_data = {'email': 'invalidemail'}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_update_user_duplicate_email(self):
        self.client.login(username=self.user.username, password=self.valid_data['password'])
        update_data = {'email': self.user.email}
        response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_delete_user_nonexistent(self):
        response = self.client.delete(f'{self.url}99999/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
