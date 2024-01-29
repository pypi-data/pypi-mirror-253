from rest_framework import serializers

from djx_account.models import OauthCredentials


class OauthCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OauthCredentials
        fields = ('id', 'user', 'access_token', 'refresh_token',
                  'expires_at', 'oauth_category')
