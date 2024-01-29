from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet

from djx_account.models import UserModel
from djx_account.serializers.registration_serializers import RegistrationSerializer


class RegistrationViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = []
    authentication_classes = []
    serializer_class = RegistrationSerializer
    queryset = UserModel.objects.all()

    def register_with_google(self, request):
        pass

