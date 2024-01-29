from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    email_confirmed = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=30)

    claims = models.JSONField(default=dict)
    additional_claims = {}

    def add_claims(self, claim_key, claim_value):
        self.additional_claims[claim_key] = claim_value

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)


UserModel = User


class UserPhoneNumbers(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    verified = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'phone_number'),)


class UserEmailAddress(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    email = models.EmailField()
    category = models.CharField(max_length=30)
    verified = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'email'),)


class OauthCredentials(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    oauth_category = models.CharField(max_length=10)
    access_token = models.TextField()
    refresh_token = models.TextField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
