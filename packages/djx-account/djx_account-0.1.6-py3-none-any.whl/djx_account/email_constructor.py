from djx_account import settings
from requests import PreparedRequest

from djx_account.utils.format_with_jinja import format_with_jinja


def create_registration_email(user):
    content_html = format_with_jinja(
        {
            'first_name': user.first_name
        }, 'templates/registration_welcome/mail.html'
    )
    recipient = user.email
    return {
        'content_plain_text': '',
        'content_html': content_html,
        'subject': 'Confirmation Email',
        'recipients': [recipient]}


def create_user_confirmation_email(user, token, redirect_to=None):
    url = redirect_to if redirect_to else settings.CLIENT_USER_CONFIRMATION_TOKEN_URL
    req = PreparedRequest()
    params = {"token": token, "email": user.email}
    req.prepare_url(url, params)
    content_html = format_with_jinja(
        {
            'url': str(req.url),
            'first_name': user.first_name
        }, 'templates/user_confirmation/mail.html'
    )
    recipient = user.email
    return {
        'content_plain_text': '',
        'content_html': content_html,
        'subject': 'Confirmation Email',
        'recipients': [recipient]}


def create_password_token_email(user, token, redirect_to):
    url = redirect_to if redirect_to else settings.CLIENT_USER_PASSWORD_RESET_TOKEN_URL
    req = PreparedRequest()
    params = {"token": token, "email": user.email}
    req.prepare_url(url, params)
    content_html = format_with_jinja(
        {
            'url': str(req.url),
            'first_name': user.first_name
        }, 'templates/password_reset/mail.html'
    )
    recipient = user.email
    return {
        'content_plain_text': '',
        'content_html': content_html,
        'subject': 'Confirmation Email',
        'recipients': [recipient]}
