from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from djx_account.serializers.user_confirmation_serializers import AskUserConfirmationSerializer, UserConfirmationSerializer


class UserConfirmationViewSet(GenericViewSet):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserConfirmationSerializer

    def get_serializer_class(self):
        if self.action == 'ask_token':
            return AskUserConfirmationSerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    @action(detail=False, methods=('post',), url_path='ask-token', url_name='ask-token')
    def ask_token(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
