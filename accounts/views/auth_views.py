from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializer import RegisterSerializer, HostRequestSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin



class AuthViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class HostRequestViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = HostRequestSerializer
    permission_classes = [IsAuthenticated]


    