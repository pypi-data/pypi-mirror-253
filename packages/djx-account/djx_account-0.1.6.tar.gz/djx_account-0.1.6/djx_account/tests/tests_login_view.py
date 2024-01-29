from rest_framework.reverse import reverse as reverse_route

from djx_account import models as account_models
from djx_account.utils.custom_tests import CustomTestCase


class LoginViewTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_login_view_accepts_valid_credentials(self):
        res = self.client.post(
            reverse_route('login-list'),
            {'email': self.user1_email, 'password': self.user1_password},
            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("access_token", res.json())

    def test_login_view_refuses_wrong_pair_username_password(self):
        res = self.client.post(
            reverse_route('login-list'),
            {'email': self.user1_email, 'password': 'self.user1_password'}, content_type='application/json')
        self.assertEqual(res.status_code, 401)
