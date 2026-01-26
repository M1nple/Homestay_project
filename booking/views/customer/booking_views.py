from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db import transaction
from booking.models import Booking 
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from booking.serializer import CustomerBookingSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin





class CustomerBookingViewSet(ModelViewSet):
    serializer_class = CustomerBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print("CUSTOMER BOOKING VIEWSET:", self.request.user)
        return Booking.objects.filter(user = self.request.user)
        
    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()

    @transaction.atomic
    @action(detail= True, methods=['post'])
    def cancel(self, request, pk = None):
        booking = self.get_object()
        if booking.status != 'PENDING':
            return Response(
                {'error':'không thể hủy booking'},
                status= status.HTTP_400_BAD_REQUEST
            )
        booking.status = 'CANCELLED'
        booking.cancelled_at = timezone.now()
        booking.save()
        return Response(
            {'message':'Hủy booking thành công'},
            status= status.HTTP_200_OK
        )
    

