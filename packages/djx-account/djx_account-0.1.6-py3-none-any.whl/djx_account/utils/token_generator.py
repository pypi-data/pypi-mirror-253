from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class CustomTokenGenerator(PasswordResetTokenGenerator):
    key_salt = "django.contrib.auth.tokens.PasswordResetTokenGenerator"
    token_timeout = settings.PASSWORD_RESET_TIMEOUT

    def __init__(self):
        super(CustomTokenGenerator, self).__init__()
