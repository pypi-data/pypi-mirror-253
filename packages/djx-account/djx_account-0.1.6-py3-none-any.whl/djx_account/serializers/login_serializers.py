from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from djx_account.models import UserModel
from djx_account.serializers.base_oauth_serializers import OauthBaseGetUrlLoginSerializer, \
    OauthBaseLoginSerializer
from djx_account.serializers.user_token_serializers import UserTokenSerializer
from djx_account.services.discord_service import DiscordService
from djx_account.services.facebook_service import FacebookService
from djx_account.services.google_service import GoogleService
from djx_account.services.microsoft_service import MicrosoftService
from djx_account.services.twitter_service import TwitterService
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import ForbiddenRequestException
from djx_account.utils.others import OauthCategory


class RefreshSerializer(UserTokenSerializer):
    refresh_token = serializers.CharField()

    def create(self, validated_data):
        refresh = RefreshToken(validated_data["refresh_token"])
        user_id = refresh['user_id']
        user = UserModel.objects.get(id=user_id)
        return user


class LoginSerializer(UserTokenSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        try:
            user = UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            raise ForbiddenRequestException(ErrorMessage.username_password_mismatch)
        if not user.check_password(password):
            raise ForbiddenRequestException(ErrorMessage.username_password_mismatch)
        return user


class LoginWithGoogleUrlSerializer(OauthBaseGetUrlLoginSerializer):
    service = GoogleService
    default_redirect_url = 'login-oauth-google'
    oauth_category = OauthCategory.google


class LoginWithGoogleSerializer(OauthBaseLoginSerializer):
    code = serializers.CharField(required=True)
    oauth_category = OauthCategory.google
    service = GoogleService
    default_redirect_url = 'login-oauth-google'


class LoginWithTwitterUrlSerializer(OauthBaseGetUrlLoginSerializer):
    url = serializers.URLField(read_only=True)
    oauth_state = serializers.JSONField(default={}, write_only=True)
    service = TwitterService
    default_redirect_url = 'login-oauth-twitter'
    oauth_category = OauthCategory.twitter


class LoginWithTwitterSerializer(OauthBaseLoginSerializer):
    oauth_token = serializers.CharField(required=True)
    oauth_verifier = serializers.CharField()
    service = TwitterService
    default_redirect_url = 'login-oauth-twitter'
    oauth_category = OauthCategory.twitter


class LoginWithMicrosoftUrlSerializer(OauthBaseGetUrlLoginSerializer):
    url = serializers.URLField(read_only=True)
    oauth_state = serializers.JSONField(default={}, write_only=True)
    service = MicrosoftService
    default_redirect_url = 'login-oauth-microsoft'
    oauth_category = OauthCategory.microsoft


class LoginWithMicrosoftSerializer(OauthBaseLoginSerializer):
    code = serializers.CharField(required=True)
    oauth_state = serializers.JSONField(default={}, write_only=True)
    service = MicrosoftService
    default_redirect_url = 'login-oauth-microsoft'
    oauth_category = OauthCategory.microsoft


class LoginWithDiscordUrlSerializer(OauthBaseGetUrlLoginSerializer):
    service = DiscordService
    default_redirect_url = 'login-oauth-discord'
    oauth_category = OauthCategory.discord


class LoginWithDiscordSerializer(OauthBaseLoginSerializer):
    code = serializers.CharField(required=True)
    oauth_category = OauthCategory.discord
    service = DiscordService
    default_redirect_url = 'login-oauth-discord'

    def post_save(self, user, validated_data, service_response):
        additional_data = service_response['additional_data']
        if "discord_guilds" in additional_data:
            user.add_claims("discord_guilds", additional_data['discord_guilds'])


class LoginWithFacebookUrlSerializer(OauthBaseGetUrlLoginSerializer):
    service = FacebookService
    default_redirect_url = 'login-oauth-facebook'
    oauth_category = OauthCategory.facebook


class LoginWithFacebookSerializer(OauthBaseLoginSerializer):
    service = FacebookService
    default_redirect_url = 'login-oauth-facebook'
    oauth_category = OauthCategory.facebook
    code = serializers.CharField(required=True)
