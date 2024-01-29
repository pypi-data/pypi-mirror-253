from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from djx_account.models import UserModel
from djx_account.serializers.user_serializers import UserSerializer, UserUpdateSerializer, ChangeUserPasswordSerializer


class UserViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == 'edit':
            return UserUpdateSerializer
        elif self.action == 'change_password':
            return ChangeUserPasswordSerializer
        return super().get_serializer_class()

    @action(detail=False, url_path='edit', url_name='edit', methods=('patch',))
    def edit(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, url_path='change-password', url_name='change-password', methods=('post',))
    def change_password(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
