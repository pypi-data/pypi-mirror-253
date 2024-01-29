from django.contrib.auth import password_validation
from rest_framework import serializers

from djx_account.models import UserModel
from djx_account.signals.senders import registration_completed


class RegistrationWithOauthSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ('first_name', 'username', 'email', 'last_name')

    def create(self, validated_data):
        email = validated_data['email']
        user, _ = UserModel.objects.get_or_create(email=email, default=validated_data)
        return user


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True, write_only=True,
        validators=[password_validation.validate_password])

    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password')

    @staticmethod
    def validate_email(value):
        if UserModel.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("user with this email address already exists.")
        return value

    def create(self, validated_data):
        email = validated_data['email'].lower()
        username = email
        user = UserModel.objects.create_user(
            username=username,
            is_active=True,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=email,
            password=validated_data['password']
        )
        registration_completed.send(sender=self.__class__, user=user)
        return user
