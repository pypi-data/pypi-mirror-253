from unittest.mock import patch

from django.test import TestCase


def send_mail(*args, **kwargs):
    return


class CustomTestCase(TestCase):

    def __init__(self, *args):
        super(CustomTestCase, self).__init__(*args)
        email_patcher = patch('djx_account.utils.mail_api.custom_send_mail', send_mail)
        email_patcher.start()
