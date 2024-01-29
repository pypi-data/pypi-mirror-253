from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#
# class DjxTokenSerializer(TokenObtainPairSerializer):
#
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         data['access_token'] = data.pop('access')
#         data['refresh_token'] = data.pop('refresh')
#         return data


class DjxLoginSerializer(LoginSerializer):
    email = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        email = attrs.get('email').lower()
        username = email
        password = attrs.get('password')

        user = self.get_auth_user(None, email, password)
        if not user:
            user = self.get_auth_user(username, None, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        # If required, is the email verified?
        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user, email=email)

        attrs['user'] = user
        return attrs


class DjxRegisterSerializer(RegisterSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        data['password1'] = data['password']
        return super().validate(data)
