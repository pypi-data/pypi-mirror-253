from rest_framework.reverse import reverse as reverse_route

from djx_account.models import UserModel
from djx_account.utils.custom_tests import CustomTestCase


class RegisterViewTestCase(CustomTestCase):

    def setUp(self) -> None:
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user = UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password='P@Sword12')

    def test_register_view_creates_user(self):
        data = {
            "password": "p@ssword2",
            "email": self.user2_email,
            "first_name": "prenom",
            "last_name": "nom"
        }
        res = self.client.post(
            reverse_route('registration-list'),
            data, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertTrue(UserModel.objects.filter(email=data['email']).exists())

    def test_register_view_doesnt_creates_user_with_duplicate_username(self):
        data = {
            "password": "p@ssword2",
            "email": self.user1_email,
            "first_name": "prenom",
            "last_name": "nom"
        }
        res = self.client.post(
            reverse_route('registration-list'),
            data, content_type='application/json')
        self.assertEqual(res.status_code, 400)
