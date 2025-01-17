from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
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
