from email import message
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from homestays.models import Room, Homestays
from rest_framework.permissions import IsAuthenticated
from homestays.serializers.room_serializer import RoomSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsHost

class HostRoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, IsHost]

    def get_queryset(self):
        return Room.objects.filter(homestay__hostID = self.request.user)
    
    # Tạo phòng mới (HOST)
    def perform_create(self, serializer):
        homestay_id = self.kwargs['homestay_id']
        homestay = get_object_or_404(Homestays, HomestayID=homestay_id)

        if homestay.hostID != self.request.user:
            raise PermissionDenied("không có quyên")
        serializer.save(homestay = homestay)
        
    # cập nhật phòng
    def perform_update(self, serializer):
        room = self.get_object()
        if room.homestay.hostID != self.request.user:
            raise PermissionDenied("bạn không có quyền sửa phòng này")
        serializer.save()
    
    # xóa phòng
    def perform_destroy(self, instance):
        if instance.homestay.hostID != self.request.user:
            raise PermissionDenied("Bạn không có quyên xóa phòng này")
        instance.delete()


    # Host get room 
    def my_rooms (self, request):
        rooms = Room.objects.filter(homestay__hostID = request.user)
        serializer = self.get_serializer(rooms, many = True)
        return Response(serializer.data)
    
