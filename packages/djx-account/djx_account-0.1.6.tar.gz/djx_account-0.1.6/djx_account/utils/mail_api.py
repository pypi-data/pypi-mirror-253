from django.core.mail import EmailMultiAlternatives


def custom_send_mail(
        subject: str, content_plain_text: str,
        recipients: [], content_html: str = None, attachments=None):

    email = EmailMultiAlternatives(
        subject=subject,
        body=content_plain_text,
        from_email=None,
        to=recipients,
    )

    if content_html:
        email.attach_alternative(content_html, "text/html")
    if attachments:
        for attachment in attachments:
            email.attach(filename=attachment['name'], content=attachment['content'])
    email.send(fail_silently=False)
