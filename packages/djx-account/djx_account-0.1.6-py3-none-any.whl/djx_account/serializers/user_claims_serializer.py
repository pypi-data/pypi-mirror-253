from rest_framework import serializers

from djx_account.models import UserModel


class UserClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email')
