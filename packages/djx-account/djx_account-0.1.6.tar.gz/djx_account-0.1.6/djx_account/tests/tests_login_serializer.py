from djx_account import models as account_models
from djx_account.serializers.login_serializers import LoginSerializer
from djx_account.utils.custom_tests import CustomTestCase
from djx_account.utils.exceptions import ForbiddenRequestException


class LoginSerializerTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_login_serializer_accepts_valid_data(self):
        data = {
            'email': self.user1_email,
            'password': self.user1_password
        }
        serializer = LoginSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)

    def test_login_serializer_returns_token_on_valid_pair(self):
        data = {
            'email': self.user1_email,
            'password': self.user1_password
        }
        serializer = LoginSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        self.assertIn('access_token', serializer.data)

    def test_login_serializer_raise_exception_on_invalid_password(self):
        data = {
            'email': self.user1_email,
            'password': 'self.user1_password'
        }
        serializer = LoginSerializer(data=data)
        serializer.is_valid()
        self.assertRaises(ForbiddenRequestException, serializer.save)

    def test_login_serializer_raise_exception_on_invalid_email(self):
        data = {
            'email': 'self.user1_email@test.org.home',
            'password': self.user1_password
        }
        serializer = LoginSerializer(data=data)
        serializer.is_valid()
        self.assertRaises(ForbiddenRequestException, serializer.save)
