from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from djx_account.serializers.login_serializers import LoginSerializer, LoginWithGoogleUrlSerializer, \
    LoginWithGoogleSerializer, RefreshSerializer, LoginWithTwitterUrlSerializer, LoginWithTwitterSerializer, \
    LoginWithMicrosoftSerializer, LoginWithMicrosoftUrlSerializer, LoginWithDiscordUrlSerializer, \
    LoginWithDiscordSerializer, LoginWithFacebookUrlSerializer, LoginWithFacebookSerializer


class LoginViewSet(GenericViewSet):
    # todo: create generic function
    permission_classes = []
    authentication_classes = []
    serializer_class = LoginSerializer

    def get_serializer_class(self):
        serializer_mapping = {
            'refresh': RefreshSerializer,
            'oauth_google': LoginWithGoogleSerializer,
            'oauth_twitter': LoginWithTwitterSerializer,
            'oauth_facebook': LoginWithFacebookSerializer,
            'oauth_microsoft': LoginWithMicrosoftSerializer,
            'oauth_discord': LoginWithDiscordSerializer,
        }
        try:
            return serializer_mapping[self.action]
        except KeyError:
            return super(LoginViewSet, self).get_serializer_class()

    def create(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    @action(detail=False, methods=('post',), url_path='refresh')
    def refresh(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    @action(detail=False, methods=('post',), url_path='google')
    def oauth_google(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('post',), url_path='twitter')
    def oauth_twitter(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('post',), url_path='facebook')
    def oauth_facebook(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('post',), url_path='microsoft')
    def oauth_microsoft(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('post',), url_path='linkedin')
    def oauth_linkedin(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('post',), url_path='discord')
    def oauth_discord(self, request):
        return self.oauth_request()

    def oauth_request(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class LoginUrlViewSet(GenericViewSet):
    # todo: create generic function
    permission_classes = []
    authentication_classes = []
    serializer_class = LoginSerializer

    def get_serializer_class(self):
        serializer_mapping = {
            'oauth_google_url': LoginWithGoogleUrlSerializer,
            'oauth_twitter_url': LoginWithTwitterUrlSerializer,
            'oauth_microsoft_url': LoginWithMicrosoftUrlSerializer,
            'oauth_discord_url': LoginWithDiscordUrlSerializer,
            'oauth_facebook_url': LoginWithFacebookUrlSerializer,
        }
        try:
            return serializer_mapping[self.action]
        except KeyError:
            return super(LoginUrlViewSet, self).get_serializer_class()

    @action(detail=False, methods=('get',), url_path='discord-url')
    def oauth_discord_url(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('get',), url_path='linkedin-url')
    def oauth_linkedin_url(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('get',), url_path='facebook-url')
    def oauth_facebook_url(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('get',), url_path='microsoft-url')
    def oauth_microsoft_url(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('get',), url_path='google-url')
    def oauth_google_url(self, request):
        return self.oauth_request()

    @action(detail=False, methods=('get',), url_path='twitter-url')
    def oauth_twitter_url(self, request):
        return self.oauth_request()

    def oauth_request(self):
        serializer = self.get_serializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
