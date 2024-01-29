from django.dispatch import Signal

registration_completed = Signal()
login_tokens_generated = Signal()
reset_password_token_generated = Signal()
reset_password_completed = Signal()
user_confirmation_token_generated = Signal()
user_confirmation_completed = Signal()
