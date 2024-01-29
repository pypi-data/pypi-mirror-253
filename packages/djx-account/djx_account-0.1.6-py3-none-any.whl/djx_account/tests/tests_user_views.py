from rest_framework.reverse import reverse as reverse_route
from rest_framework_simplejwt.tokens import AccessToken

from djx_account.models import UserModel
from djx_account.utils.custom_tests import CustomTestCase


class UserViewTestCase(CustomTestCase):

    def setUp(self) -> None:
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)
        self.token1 = AccessToken.for_user(self.user)

    def test_user_view_return_user_profile(self):
        res = self.client.get(
            reverse_route(
                'user-detail', kwargs={'pk': 'me'},
            ),
            HTTP_AUTHORIZATION='Bearer %s' % self.token1,
        )
        self.assertEqual(200, res.status_code)

    def test_user_view_edit_user_profile(self):
        new_name = "new_name"
        res = self.client.patch(
            reverse_route(
                'user-edit'
            ),
            data={"first_name": new_name}, content_type='application/json',
            HTTP_AUTHORIZATION='Bearer %s' % self.token1,
        )
        exist = UserModel.objects.filter(first_name=new_name, email=self.user1_email)
        self.assertEqual(200, res.status_code)
        self.assertTrue(exist)

    def test_user_view_change_user_password(self):
        new_password = "newP@ssword123"
        res = self.client.post(
            reverse_route(
                'user-change-password'
            ),
            data={
                "old_password": self.user1_password,
                "new_password": new_password}, content_type='application/json',
            HTTP_AUTHORIZATION='Bearer %s' % self.token1,
        )
        self.user.refresh_from_db()
        is_changed = self.user.check_password(new_password)
        self.assertEqual(200, res.status_code)
        self.assertTrue(is_changed)
