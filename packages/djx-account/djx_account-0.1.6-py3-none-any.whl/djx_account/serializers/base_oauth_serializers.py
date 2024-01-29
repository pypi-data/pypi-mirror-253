from django.urls import reverse as reverse_url
from rest_framework import serializers

from djx_account import settings
from djx_account.models import OauthCredentials, UserModel
from djx_account.serializers.oauth_credentials_serializers import OauthCredentialSerializer
from djx_account.serializers.user_token_serializers import UserTokenSerializer
from djx_account.signals.senders import registration_completed
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException


class OauthBaseSerializer(serializers.Serializer):
    oauth_category = None
    service = None
    default_redirect_url = None
    redirect_to = serializers.URLField(write_only=True, required=False)

    def get_default_redirect_to_value(self, value):
        if value is None:
            req = self.context['request']
            url = reverse_url(self.default_redirect_url)
            value = req.build_absolute_uri(url)
        return value

    def validated_redirect_to(self, value):
        return self.get_default_redirect_to_value(value)


class OauthBaseLoginSerializer(OauthBaseSerializer):

    def save_oauth_credentials(self, user, credentials):
        if not credentials:
            return
        try:
            oauth_credentials_instance = OauthCredentials.objects.get(
                user=user,
                oauth_category=self.oauth_category
            )
        except OauthCredentials.DoesNotExist:
            oauth_credentials_instance = None
        serializer = OauthCredentialSerializer(
            instance=oauth_credentials_instance,
            data={
                **credentials, "user": user.id,
                "oauth_category": self.oauth_category
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, validated_data):
        redirect_to = validated_data.get('redirect_to', None)
        redirect_to = self.get_default_redirect_to_value(redirect_to)
        response = self.service.check_token(redirect_uri=redirect_to, **validated_data)
        user_data = response['user']
        user_credentials = response['credentials'] if "credentials" in response else None

        if settings.CREATE_USER_ON_LOGIN:
            user, created = UserModel.objects.get_or_create(
                email=user_data['email'],
                is_active=True,
                defaults=user_data
            )
            if created:
                registration_completed.send(sender=self.__class__, user=user)
        else:
            try:
                user = UserModel.objects.get(
                    email=user_data['email']
                )
            except UserModel.DoesNotExist:
                raise BadRequestException(ErrorMessage.user_not_found)
        self.save_oauth_credentials(user, user_credentials)
        self.post_save(user, validated_data, response)
        return user

    def post_save(self, user, validated_data, service_response):
        pass

    def to_representation(self, instance):
        return UserTokenSerializer().to_representation(instance)


class OauthBaseGetUrlLoginSerializer(OauthBaseSerializer):
    url = serializers.URLField(read_only=True)

    def create(self, validated_data):
        redirect_to = validated_data.get('redirect_to', None)
        redirect_to = self.get_default_redirect_to_value(redirect_to)
        url = self.service.get_url(redirect_uri=redirect_to, **validated_data)
        return {"url": url}
