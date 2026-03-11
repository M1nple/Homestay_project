from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializer import RegisterSerializer, HostRequestSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from rest_framework.views import APIView
from rest_framework.response import Response


class AuthViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class HostRequestViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = HostRequestSerializer
    permission_classes = [IsAuthenticated]

class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        })