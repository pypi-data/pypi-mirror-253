from django.contrib.auth import password_validation
from requests import PreparedRequest
from rest_framework import serializers

from djx_account import settings
from djx_account.models import UserModel
from djx_account.signals.senders import reset_password_token_generated, reset_password_completed
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException
from djx_account.utils.others import redirect_url_validators
from djx_account.utils.token_generator import CustomTokenGenerator


class AskResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    redirect_to = serializers.URLField(write_only=True, required=False, validators=[redirect_url_validators])

    @staticmethod
    def generate_password_reset_url(user, redirect_to):
        token = ResetPasswordToken().make_token(user)
        url = redirect_to if redirect_to else settings.CLIENT_USER_PASSWORD_RESET_TOKEN_URL
        req = PreparedRequest()
        params = {"token": token, "email": user.email}
        req.prepare_url(url, params)
        return req.url

    def create(self, validated_data):
        email = validated_data['email']
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            pass
        else:
            try:
                redirect_to = validated_data['redirect_to']
            except KeyError:
                redirect_to = None
            url = self.generate_password_reset_url(user, redirect_to)
            reset_password_token_generated.send(sender=self.__class__, user=user, url=url)
        return email


class CheckTokenPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    token = serializers.CharField(write_only=True)

    @staticmethod
    def _check_token(user, validated_data):
        return ResetPasswordToken().check_token(user, validated_data['token'])

    @staticmethod
    def get_user(validated_data):
        email = validated_data['email']
        try:
            return UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            return None

    def create(self, validated_data):
        user = self.get_user(validated_data)
        if user is not None and self._check_token(user, validated_data):
            return True
        raise BadRequestException(detail=ErrorMessage.invalid_token_password)


class ResetPasswordSerializer(CheckTokenPasswordSerializer):
    password = serializers.CharField(validators=[password_validation.validate_password], write_only=True)

    def create(self, validated_data):
        user = self.get_user(validated_data)
        if user is not None and self._check_token(user, validated_data):
            user.set_password(validated_data['password'])
            user.save()
            reset_password_completed.send(sender=self.__class__, user=user)
            return ''
        raise BadRequestException(detail=ErrorMessage.invalid_token_password)


class ResetPasswordToken(CustomTokenGenerator):
    token_timeout = settings.USER_PASSWORD_RESET_TOKEN_TTL

    def __init__(self):
        super(CustomTokenGenerator, self).__init__()

    def _make_hash_value(self, data: UserModel, timestamp):
        text = f"{data.email}{data.password}"
        return text
