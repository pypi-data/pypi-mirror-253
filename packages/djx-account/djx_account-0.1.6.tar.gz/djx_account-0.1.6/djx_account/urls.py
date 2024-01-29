from django.urls import path, include
from rest_framework.routers import DefaultRouter

from djx_account.views.login_views import LoginUrlViewSet, LoginViewSet
from djx_account.views.registration_views import RegistrationViewSet
from djx_account.views.reset_password_views import ResetPasswordViewSet
from djx_account.views.user_confirmation_views import UserConfirmationViewSet
from djx_account.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'registration', RegistrationViewSet, basename='registration')
router.register(r'login', LoginUrlViewSet, basename='login-url')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'user', UserViewSet, basename='user')
router.register(r'reset-password', ResetPasswordViewSet, basename='reset-password')
router.register(r'user-confirmation', UserConfirmationViewSet, basename='user-confirmation')

urlpatterns = [
    path('', include(router.urls)),
    #
    # path('login/google/', GoogleLogin.as_view(), name='google_login'),
    # path('login/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    # # path('login/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    # #
    # path('connect/google/', GoogleConnect.as_view(), name='google_connect'),
    # path('login/', LoginView.as_view(), name='rest_login'),
    #
    # # path('registration/', include('dj_rest_auth.registration.urls'))
    # path(
    #     'socialaccounts/<int:pk>/disconnect/',
    #     SocialAccountDisconnectView.as_view(),
    #     name='social_account_disconnect'
    # ),
    # path("socialaccounts/", SocialAccountListView.as_view(), name="socialaccount_connections", ),
    # path('auth/facebook/socialaccount_signup/', allauth_views.signup, name='socialaccount_signup'),

]
