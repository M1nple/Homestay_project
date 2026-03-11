from turtle import home
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from homestays.models import HomestayImage, Homestays
from rest_framework.permissions import IsAuthenticated
from homestays.serializers.homestay_serializer import HomestaySerializer
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsHost
from booking.models import Booking
from rest_framework.exceptions import ValidationError


class HostHomestayViewSet(ModelViewSet):
    queryset = Homestays.objects.all()
    serializer_class = HomestaySerializer
    permission_classes = [IsAuthenticated, IsHost]
    parser_classes = [MultiPartParser, FormParser, JSONParser]   

    def get_queryset(self):
        return Homestays.objects.filter(hostID = self.request.user)
    
    # create
    def perform_create(self, serializer):
        print("bắt đ")
        # lưu homestay
        homestay = serializer.save(hostID = self.request.user)
        print("đã lưu homestay", homestay.HomestayID)
        # lưu ảnh 
        images = self.request.FILES.getlist('images')
        print("FILES:" , images)
        for image in images:
            HomestayImage.objects.create(
                homestay = homestay, 
                image = image
            )
        print("ok")

    # update
    def perform_update(self, serializer):
 
        homestay = serializer.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            HomestayImage.objects.create(
                homestay = homestay, 
                image = image
            )

    # delete homestay
    def perform_destroy(self, instance): #perform_destroy() trong DRF KHÔNG dùng để trả Response nên kh return message
        has_booking = Booking.objects.filter(
            room__homestay=instance,
            status__in=['PENDING', 'CONFIRMED', 'PAID']
        ).exists()

        if has_booking:
            raise ValidationError(
                "Không thể xóa homestay vì đang có booking."
            )
        if instance.hostID != self.request.user:
            raise PermissionDenied("Bạn không có quyên xóa homestay này")
        
        instance.delete()     

class HostHomestayImageViewSet(ModelViewSet):
    queryset = HomestayImage.objects.all()
    permission_classes = [IsAuthenticated, IsHost]
    def destroy(self, request, *args, **kwargs): # override perform_destroy nên có thế return message
        image = self.get_object()
        if image.homestay.hostID != self.request.user:
            raise PermissionDenied('Bạn không có quyền xóa ảnh này')
        # xoa file vật lý
        image.image.delete(save = False)
        # xóa file trong db
        image.delete()
        return Response(
            {'message' : 'Xóa ảnh thành công'},
            status= status.HTTP_200_OK
        )
