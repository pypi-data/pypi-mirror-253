from djx_account import models as account_models
from djx_account.models import UserModel
from djx_account.serializers.registration_serializers import RegistrationSerializer
from djx_account.utils.custom_tests import CustomTestCase


class RegisterSerializerTestCase(CustomTestCase):

    def setUp(self):
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user = account_models.UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password='P@Sword12')

    def test_registration_serializer_accepts_valid_data(self):
        serializer = RegistrationSerializer(
            data={
                'email': self.user2_email,
                'last_name': 'last_name',
                'password': 'P@Sword12',
                'first_name': 'prenom'
            })
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_registration_serializer_refuse_data_for_existing_user(self):
        serializer = RegistrationSerializer(
            data={
                'email': self.user1_email,
                'last_name': 'last_name',
                'password': 'P@Sword12',
                'first_name': 'prenom'
            })
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)

    def test_registration_serializer_create_user_with_valid_data(self):
        serializer = RegistrationSerializer(
            data={
                'email': self.user2_email,
                'last_name': 'last_name',
                'password': 'P@Sword12',
                'first_name': 'prenom'
            })
        serializer.is_valid()
        serializer.save()
        exist = UserModel.objects.filter(email=self.user2_email).exists()
        self.assertTrue(exist)
