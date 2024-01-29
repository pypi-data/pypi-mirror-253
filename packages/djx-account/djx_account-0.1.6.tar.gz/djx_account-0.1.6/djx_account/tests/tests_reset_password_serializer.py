from djx_account import models as account_models
from djx_account.serializers.reset_password_serializers import AskResetPasswordSerializer, CheckTokenPasswordSerializer, \
    ResetPasswordToken, ResetPasswordSerializer
from djx_account.utils.custom_tests import CustomTestCase


class AskResetPasswordSerializerTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_ask_reset_password_serializer_accepts_valid_data(self):
        serializer = AskResetPasswordSerializer(data={"email": "mail@test.org.home"})
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class CheckTokenPasswordSerializerTestCase(CustomTestCase):
    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_check_reset_password_valid_expected_values(self):
        token = ResetPasswordToken().make_token(self.user)
        serializer = CheckTokenPasswordSerializer(data={
            'email': self.user1_email,
            'token': token
        })
        serializer.is_valid()
        self.assertTrue(serializer.save())


class ResetPasswordSerializerTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_reset_password_serializer_accepts_valid_data(self):
        data = {
            'email': self.user1_email,
            'password': 'p@12ssword',
            'token': '...'
        }
        serializer = ResetPasswordSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)

    def test_reset_password_serializer_change_password(self):
        new_password = 'p@12ssword'
        data = {
            'email': self.user1_email,
            'password': new_password,
            'token': ResetPasswordToken().make_token(self.user)
        }
        serializer = ResetPasswordSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_password))