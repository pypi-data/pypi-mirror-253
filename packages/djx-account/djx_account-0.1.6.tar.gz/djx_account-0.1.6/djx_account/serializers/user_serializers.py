from django.contrib.auth import password_validation
from rest_framework import serializers

from djx_account.models import UserModel
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'id')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name')


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(
        required=True, write_only=True,
        validators=[password_validation.validate_password])
    new_password = serializers.CharField(
        required=True, write_only=True,
        validators=[password_validation.validate_password])

    class Meta:
        model = UserModel
        fields = ('old_password', 'new_password')

    def update(self, instance: UserModel, validated_data):
        old_password = validated_data['old_password']
        new_password = validated_data['new_password']
        if not instance.check_password(old_password):
            raise BadRequestException(detail=ErrorMessage.password_mismatch)
        instance.set_password(new_password)
        instance.save()
        return instance
