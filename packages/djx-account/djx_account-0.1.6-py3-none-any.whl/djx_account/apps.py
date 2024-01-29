from django.apps import AppConfig


class DjangoAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djx_account'

    def ready(self):
        from .signals import receivers
