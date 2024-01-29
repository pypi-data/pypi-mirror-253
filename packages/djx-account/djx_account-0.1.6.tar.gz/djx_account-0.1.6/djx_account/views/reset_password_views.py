from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from djx_account.serializers.reset_password_serializers import AskResetPasswordSerializer, CheckTokenPasswordSerializer, \
    ResetPasswordSerializer


class ResetPasswordViewSet(GenericViewSet):
    permission_classes = []
    authentication_classes = []
    serializer_class = ResetPasswordSerializer

    def get_serializer_class(self):
        if self.action == 'check_token':
            return CheckTokenPasswordSerializer
        elif self.action == 'ask_token':
            return AskResetPasswordSerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(data=instance)

    @action(detail=False, methods=('post',), url_path='check-token', url_name='check-token')
    def check_token(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(data=instance)

    @action(detail=False, methods=('post',), url_path='ask-token', url_name='ask-token')
    def ask_token(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(data=instance)
