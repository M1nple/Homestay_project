from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from homestays.models import Homestays
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from homestays.serializers.homestay_serializer import HomestaySerializer


class PublicHomestayViewSet(ReadOnlyModelViewSet):
    serializer_class = HomestaySerializer
    permission_classes = [AllowAny]

    # Public khách có thể xem tất cả các homestay
    def get_queryset(self):
        return Homestays.objects.all()
    
