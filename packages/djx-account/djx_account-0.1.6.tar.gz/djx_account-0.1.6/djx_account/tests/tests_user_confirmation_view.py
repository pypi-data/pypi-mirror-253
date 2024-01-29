from rest_framework.reverse import reverse as reverse_route

from djx_account.models import UserModel
from djx_account.serializers.user_confirmation_serializers import UserConfirmationToken
from djx_account.utils.custom_tests import CustomTestCase


class UserConfirmationViewSetTestCase(CustomTestCase):

    def setUp(self) -> None:
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user = UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password='P@Sword12')

    def test_user_confirmation_view_confirm_user_when_valid_payload(self):
        data = {
            'email': self.user1_email,
            'token': UserConfirmationToken().make_token(self.user)
        }
        response = self.client.post(reverse_route('user-confirmation-list'), data=data,
                                    content_type="application/json")
        self.assertEqual(200, response.status_code)
