from requests import PreparedRequest
from rest_framework import serializers

from djx_account import settings
from djx_account.models import UserModel
from djx_account.signals.senders import user_confirmation_token_generated, user_confirmation_completed
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException
from djx_account.utils.others import redirect_url_validators
from djx_account.utils.token_generator import CustomTokenGenerator


class AskUserConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    redirect_to = serializers.URLField(write_only=True, required=False, validators=[redirect_url_validators])

    @staticmethod
    def get_user(validated_data):
        email = validated_data['email']
        try:
            return UserModel.objects.get(email__iexact=email, email_confirmed=False)
        except UserModel.DoesNotExist:
            return None

    @staticmethod
    def generate_user_confirmation_url(user: UserModel, redirect_to: str):
        token = UserConfirmationToken().make_token(user)
        url = redirect_to if redirect_to else settings.CLIENT_USER_CONFIRMATION_TOKEN_URL
        req = PreparedRequest()
        params = {"token": token, "email": user.email}
        req.prepare_url(url, params)
        return req.url

    def create(self, validated_data):
        user = self.get_user(validated_data)
        try:
            redirect_to = validated_data['redirect_to']
        except KeyError:
            redirect_to = None
        if user is not None and not user.email_confirmed:
            url = self.generate_user_confirmation_url(user, redirect_to)
            user_confirmation_token_generated.send(sender=self.__class__, user=user, url=url)
        return ''


class UserConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    token = serializers.CharField(write_only=True)

    @staticmethod
    def get_user(validated_data):
        email = validated_data['email']
        try:
            return UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            return None

    def create(self, validated_data):
        user = self.get_user(validated_data)
        if user is not None and UserConfirmationToken().check_token(user, validated_data['token']):
            user.email_confirmed = True
            user.save()
            user_confirmation_completed.send(sender=self.__class__, user=user)
            return ''
        raise BadRequestException(ErrorMessage.invalid_token_email_confirmation)


class UserConfirmationToken(CustomTokenGenerator):
    token_timeout = settings.USER_CONFIRMATION_TOKEN_TTL

    def _make_hash_value(self, data: UserModel, timestamp):
        text = f"{data.email}{data.is_active}{data.email_confirmed}"
        return text
