from djx_account.models import UserModel
from djx_account.serializers.user_serializers import ChangeUserPasswordSerializer, UserUpdateSerializer
from djx_account.utils.custom_tests import CustomTestCase


class UserSerializerTestCase(CustomTestCase):

    def setUp(self) -> None:
        self.user1_email = "mail1@test.org.home"
        self.user2_email = "mail2@test.org.home"
        self.user1_password = "P@Sword12"
        self.user = UserModel.objects.create_user(
            username=self.user1_email,
            email=self.user1_email,
            password=self.user1_password)

    def test_change_password_change_expected_values(self):
        new_password = "newP@ssword123"
        data = {
            "new_password": "newP@ssword123",
            "old_password": self.user1_password
        }
        serializer = ChangeUserPasswordSerializer(instance=self.user, data=data)
        serializer.is_valid()
        serializer.save()

        self.user.refresh_from_db()
        valid = self.user.check_password(new_password)
        self.assertTrue(valid)

    def test_edit_user_change_expected_values(self):
        new_name = "new_name"
        data = {
            'first_name': new_name
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data)
        serializer.is_valid()
        serializer.save()
        self.user.refresh_from_db()

        self.assertEqual(new_name, self.user.first_name)