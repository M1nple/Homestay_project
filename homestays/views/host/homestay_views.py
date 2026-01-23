from turtle import home
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser
# from homestay_project.api import serializer
from homestays.models import HomestayImage, Room, Homestays
from rest_framework.permissions import IsAuthenticated
from homestays.serializers.homestay_serializer import HomestaySerializer
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsHost


class HostHomestayViewSet(ModelViewSet):
    serializer_class = HomestaySerializer
    permission_classes = [IsAuthenticated, IsHost]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Homestays.objects.filter(hostID = self.request.user)
    
    # Host get homestay
    def my_homestay(sefl, request):
        homestays = Homestays.objects.filter(hostID = request.user)
        serializer = sefl.get_serializer(homestays, many = True)
        return Response(serializer.data)
    
    # create
    def perform_create(self, serializer):
        # lưu homestay
        homestay = serializer.save(hostID = self.request.user)
        # lưu ảnh 
        images = self.request.FILES.getlist('images')
        for image in images:
            HomestayImage.objects.create(
                homestay = homestay, 
                image = image
            )

    # update
    def perform_update(self, serializer):
        homestay = self.get_object()
        if homestay.hostID != self.request.user:
            raise PermissionDenied ("bạn không có quyền sửa homestay này")
        serializer.save()

    # delete
    def perform_destroy(self, instance):
        if instance.hostID != self.request.user:
            raise PermissionDenied("Bạn không có quyên xóa homestay này")
        instance.delete()
        