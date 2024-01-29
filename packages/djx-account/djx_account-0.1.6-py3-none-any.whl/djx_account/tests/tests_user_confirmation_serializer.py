from djx_account import models as account_models
from djx_account.serializers.user_confirmation_serializers import AskUserConfirmationSerializer, UserConfirmationSerializer, \
    UserConfirmationToken
from djx_account.utils.custom_tests import CustomTestCase


class UserConfirmationSerializerTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "email@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_ask_user_confirmation_token_serializer_accepts_valid_data(self):
        serializer = AskUserConfirmationSerializer(data={"email": "mail@test.org.home"})
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


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
            'token': UserConfirmationToken().make_token(self.user)
        }
        serializer = UserConfirmationSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        serializer.save()
        self.user.refresh_from_db()
        self.assertTrue(self.user.email_confirmed)
