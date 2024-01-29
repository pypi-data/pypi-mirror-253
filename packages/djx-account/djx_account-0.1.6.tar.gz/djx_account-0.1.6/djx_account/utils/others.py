from django.conf import settings
from rest_framework import serializers

from djx_account.utils.error_messages import ErrorMessage


def redirect_url_validators(value):
    if value not in settings.REDIRECT_URLS:
        raise serializers.ValidationError(ErrorMessage.invalid_redirect_url)


class OauthCategory:
    microsoft = 'microsoft'
    twitter = 'twitter'
    facebook = 'facebook'
    google = 'google'
    discord = 'discord'
