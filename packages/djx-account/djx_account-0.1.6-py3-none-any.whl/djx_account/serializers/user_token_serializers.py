from django.contrib.auth import login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from djx_account import settings
from djx_account.serializers.user_claims_serializer import UserClaimSerializer
from djx_account.signals.senders import login_tokens_generated


class UserTokenSerializer(serializers.Serializer):

    def to_representation(self, instance):
        claims = UserClaimSerializer(instance=instance).data
        token = AccessToken.for_user(instance)
        for key in claims:
            token[key] = claims[key]
        token['additional_claims'] = instance.additional_claims
        refresh_token = RefreshToken.for_user(instance)
        login_tokens_generated.send(sender=self.__class__, user_instance=instance)
        if settings.ALLOW_SESSION:
            login(self.context['request'], instance)

        return {
            "access_token": str(token),
            "refresh_token": str(refresh_token)
        }

    def update(self, instance, validated_data):
        raise NotImplemented

    def create(self, validated_data):
        raise NotImplemented
