# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
#
#
# class UserTest(APITestCase):
#     def setUp(self):
#         self.client: APIClient = APIClient()
#         self.valid_data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'Password123',
#         }
#         self.register_url = '/api/v1/auth/register'
#
#     def test_users_can_register_with_valid_details(self):
#         response = self.client.post('/api/v1/auth/register', self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual('testuser@example.com', response.data['email'])
#         self.assertEqual('testuser', response.data['username'])
#         self.assertEqual('Male', response.data['gender'])
#
#     def test_user_registration_with_invalid_details_fails(self):
#         self.valid_data['email'] = 'mail'
#         response = self.client.post('/api/v1/auth/register', self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.valid_data['email'] = 'mailer@mail.com'
#         self.valid_data['password'] = 'pass'
#         response = self.client.post('/api/v1/auth/register', self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.valid_data['password'] = '1234'
#         response = self.client.post('/api/v1/auth/register', self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.valid_data['password'] = 'Passwo12'
#         response = self.client.post('/api/v1/auth/register', self.valid_data)
#         self.assertIn('date_joined', response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_user_login_after_registration(self):
#
#         pass
#     # def test_user_can_update_profile(self):
#     #     data = {
#     #         'email': 'name@gmail.com',
#     #         'password': '      ',
#     #         'username': 'username'
#     #     }
#     #     registration_response = self.client.post('/auth/users', data, 'json')
#     #     self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)
#     #     registration_response = self.client.post('/auth/users', data, 'json')
#     #     self.assertEqual(registration_response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     data['email'] = 'name1@gmail.com'
#     #     self.assertEqual(registration_response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     data['password']= 'name1@gmail.67'
#     #     self.assertEqual(registration_response.status_code,status.HTTP_400_BAD_REQUEST)
#     #
#     # def test_create_user_success(self):
#     #     data = {
#     #         'username': 'newuser',
#     #         'email': 'newuser@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #     self.assertEqual(response.data['username'], 'newuser')
#     #
#     # def test_create_user_missing_field(self):
#     #     data = {
#     #         'username': 'newuser'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('email', response.data)
#     #     self.assertIn('password', response.data)
#     #
#     # def test_create_user_invalid_email(self):
#     #     data = {
#     #         'username': 'newuser',
#     #         'email': 'invalidemail',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('email', response.data)
#     #
#     # def test_create_user_password_too_short(self):
#     #     data = {
#     #         'username': 'newuser',
#     #         'email': 'newuser@example.com',
#     #         'password': '123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('password', response.data)
#     #
#     # def test_get_user_details_authenticated(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     response = self.client.get(f'{self.url}{self.user.id}/', format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(response.data['username'], self.user.username)
#     #
#     # def test_get_user_details_unauthenticated(self):
#     #     response = self.client.get(f'{self.url}{self.user.id}/', format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#     #
#     # def test_update_user_success(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     update_data = {'email': 'newemail@example.com'}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(response.data['email'], 'newemail@example.com')
#     #
#     # def test_delete_user_success(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     response = self.client.delete(f'{self.url}{self.user.id}/', format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#     #
#     # def test_update_user_invalid_field(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     update_data = {'username': ''}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('username', response.data)
#     #
#     # def test_server_error(self):
#     #     response = self.client.get(f'{self.url}nonexistent/', format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
#     #
#     # def test_edge_case_username_length(self):
#     #     long_username = 'a' * 255
#     #     data = {
#     #         'username': long_username,
#     #         'email': 'longusername@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #     self.assertEqual(response.data['username'], long_username)
#     #
#     # def test_edge_case_empty_request(self):
#     #     response = self.client.post(self.url, {}, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('username', response.data)
#     #     self.assertIn('email', response.data)
#     #     self.assertIn('password', response.data)
#     #
#     # def test_create_user_username_max_length(self):
#     #     max_length_username = 'a' * 150
#     #     data = {
#     #         'username': max_length_username,
#     #         'email': 'maxusername@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #
#     # def test_create_user_username_empty(self):
#     #     data = {
#     #         'username': '',
#     #         'email': 'emptyusername@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('username', response.data)
#     #
#     # def test_create_user_duplicate_username(self):
#     #     data = {
#     #         'username': 'testuser',
#     #         'email': 'duplicate@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('username', response.data)
#     #
#     # def test_create_user_email_already_exists(self):
#     #     data = {
#     #         'username': 'newuser',
#     #         'email': self.user.email,
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('email', response.data)
#     #
#     # def test_edge_case_password_length(self):
#     #     long_password = 'a' * 255
#     #     data = {
#     #         'username': 'newuser',
#     #         'email': 'newuser@example.com',
#     #         'password': long_password
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #
#     # def test_invalid_patch_request(self):
#     #     update_data = {'nonexistent_field': 'test'}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #
#     # def test_update_user_nonexistent_field(self):
#     #     update_data = {'nonexistent_field': 'value'}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #
#     # def test_create_user_special_characters_username(self):
#     #     data = {
#     #         'username': '@user#',
#     #         'email': 'specialchar@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #
#     # def test_create_user_special_characters_email(self):
#     #     data = {
#     #         'username': 'user1',
#     #         'email': 'user!@example.com',
#     #         'password': 'password123'
#     #     }
#     #     response = self.client.post(self.url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #
#     # def test_update_user_invalid_email(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     update_data = {'email': 'invalidemail'}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('email', response.data)
#     #
#     # def test_update_user_duplicate_email(self):
#     #     self.client.login(username=self.user.username, password=self.valid_data['password'])
#     #     update_data = {'email': self.user.email}
#     #     response = self.client.patch(f'{self.url}{self.user.id}/', update_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('email', response.data)
#     #
#     # def test_delete_user_nonexistent(self):
#     #     response = self.client.delete(f'{self.url}99999/', format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class UserManagementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = "/auth/users/"
        self.login_url = "/auth/jwt/create/"
        self.reset_password_url = "/auth/users/reset_password/"
        self.reset_password_confirm_url = "/auth/users/reset_password_confirm/"
        self.activate_url = "/auth/users/activation/"
        self.set_password_url = "/auth/users/set_password/"
        self.me_url = "/auth/users/me/"

        self.user_data = {
            "username": "testuser",
            "password": "securepassword123",
            "first_name": "Test",
            "last_name": "User",
            "gender": "M",
        }
        self.user = User.objects.create_user(**self.user_data)

    def get_jwt_token(self, username, password):
        response = self.client.post(self.login_url, {"username": username, "password": password})
        return response.data["access"]

    def test_registration_with_duplicate_username(self):
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

    def test_registration_with_invalid_email(self):
        invalid_user_data = self.user_data.copy()
        invalid_user_data["email"] = "invalid-email"
        response = self.client.post(self.register_url, invalid_user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_profile_picture_upload_invalid_format(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_jwt_token('testuser', 'securepassword123')}")
        invalid_file = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")
        response = self.client.put(self.me_url, {"profile_picture": invalid_file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_reset_with_invalid_token(self):
        response = self.client.post(self.reset_password_confirm_url, {
            "uid": "invalid_uid",
            "token": "invalid_token",
            "new_password": "newsecurepassword123"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("token", response.data)

    def test_email_verification_expired_token(self):
        response = self.client.post(self.activate_url, {"uid": "invalid_uid", "token": "expired_token"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_unverified_account(self):
        unverified_user = User.objects.create_user(username="unverifieduser", password="password123", is_active=False)
        response = self.client.post(self.login_url, {"username": unverified_user.username, "password": "password123"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("non_field_errors", response.data)

    def test_password_change_without_current_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_jwt_token('testuser', 'securepassword123')}")
        response = self.client.post(self.set_password_url, {"new_password": "newpassword123"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("current_password", response.data)

    def test_registration_with_extremely_long_fields(self):
        long_data = self.user_data.copy()
        long_data["username"] = "a" * 256
        response = self.client.post(self.register_url, long_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

    def test_invalid_gender_choice(self):
        invalid_data = self.user_data.copy()
        invalid_data["gender"] = "X"  # Invalid gender choice
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("gender", response.data)

    def test_large_profile_picture_upload(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_jwt_token('testuser', 'securepassword123')}")
        large_file = SimpleUploadedFile("large_image.jpg", b"a" * 10 * 1024 * 1024, content_type="image/jpeg")
        response = self.client.put(self.me_url, {"profile_picture": large_file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_brute_force_protection(self):
        for _ in range(10):
            response = self.client.post(self.login_url, {"username": "testuser", "password": "wrongpassword"})
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(self.login_url, {"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
