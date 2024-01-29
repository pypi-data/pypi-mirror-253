from rest_framework.reverse import reverse as reverse_route

from djx_account.models import UserModel
from djx_account.serializers.reset_password_serializers import ResetPasswordToken
from djx_account.utils.custom_tests import CustomTestCase


class ResetPasswordViewSetTestCase(CustomTestCase):

    def setUp(self) -> None:
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user = UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password='P@Sword12')

    def test_reset_password_view_set_change_password_when_valid_payload(self):
        new_password = 'p@12ssword'
        data = {
            'email': self.user1_email,
            'password': new_password,
            'token': ResetPasswordToken().make_token(self.user)
        }
        response = self.client.post(reverse_route('reset-password-ask-token'), data=data,
                                    content_type="application/json")
        self.assertEqual(200, response.status_code)

    def test_check_reset_password_view_set_return_true_with_valid_payload(self):
        data = {
            'email': self.user1_email,
            'token': ResetPasswordToken().make_token(self.user)
        }
        response = self.client.post(reverse_route('reset-password-check-token'), data=data,
                                    content_type="application/json")
        self.assertEqual(200, response.status_code)
