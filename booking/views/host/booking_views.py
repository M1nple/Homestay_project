from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from booking.serializer import BookingSerializer
from rest_framework.viewsets import ModelViewSet
from booking.models import Booking
from accounts.permissions import IsHost
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response


class HostBookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsHost]

    def get_queryset(self):
        return Booking.objects.filter(room_id__homestay__hostID = self.request.user)

    @action(detail = True, methods=['post'])
    def accept(self, request, pk=None):
        host_accept = self.get_object()
        host_accept = get_object_or_404(Booking, pk=pk, status = 'PENDING')

        host_accept.status = 'CONFIRMED'
        host_accept.confirm_at = timezone.now()
        host_accept.save()

        return Response(
            {'message':'Đã xác nhận'},
            status= status.HTTP_200_OK
        )
    
    @action(detail= True, methods=['post'])
    def reject(self, request, pk=None):
        host_accept = self.get_object()
        host_accept = get_object_or_404(Booking, pk=pk, status = 'PENDING')

        host_accept.status = 'CANCELLED'
        host_accept.confirm_at = timezone.now()
        host_accept.save()

        return Response(
            {'message':'Đã hủy'},
            status= status.HTTP_200_OK
        )
    