from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from djx_account import settings
from djx_account.models import UserModel


class Command(BaseCommand):
    help = 'Create admin'

    def handle(self, *args, **options):
        username = settings.DEFAULT_ADMIN_USERNAME
        email = settings.DEFAULT_ADMIN_EMAIL
        password = settings.DEFAULT_ADMIN_PASSWORD
        UserModel.objects.update_or_create(
            username=username, email=email,
            defaults={'password': make_password(password), 'is_staff': True, 'is_superuser': True})
