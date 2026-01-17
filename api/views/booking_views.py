from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from api.serializers.booking_serializer import BookingCreateSerializer, BookingSerializer
from booking.models import Booking
from homestays.models import Room
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from api.permissions import IsAdmin, IsHost

# ADMIN or HOST
# GET All Bookings API View by Admin or Host
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin | IsHost])
def get_all_bookings_api(request):
    if IsHost().has_permission(request, None):
        bookings = Booking.objects.filter(room_id__homestay__hostID=request.user)
    else:
        bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Accept Booking API View by Host
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsHost])
def accept_booking_api(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, room_id__homestay__hostID=request.user)
    if booking.status != 'PENDING':
        return Response({'error': 'không thể chấp nhận.'}, status=status.HTTP_400_BAD_REQUEST)
    booking.status = 'CONFIRMED'
    booking.save()
    return Response({'message': 'Booking đã được chấp nhận.'}, status=status.HTTP_200_OK)

# Reject Booking API View by Host
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsHost])
def reject_booking_api(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, room_id__homestay__hostID=request.user)
    if booking.status != 'PENDING':
        return Response({'error': 'không thể từ chối.'}, status=status.HTTP_400_BAD_REQUEST)
    booking.status = 'CANCELLED'
    booking.save()
    return Response({'message': 'Booking đã bị từ chối.'}, status=status.HTTP_200_OK)


# CUSTOMER
# GET booking by customer API View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_bookings_api(request):
    bookings = Booking.objects.filter(user_id=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create Booking API View
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking_api(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    serializer = BookingCreateSerializer(
        data=request.data, 
        context={'room': room, 'request': request}
        )
    if serializer.is_valid():
        serializer.save(
            # user_id =request.user,
            # room_id =room,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT Booking API View
@csrf_exempt
# @api_view(['PUT']) # Put để cập nhật toàn bộ
@api_view(['PATCH']) # Sửa thành PATCH để chỉ cập nhật một phần
@permission_classes([IsAuthenticated])
def update_booking_api(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user_id=request.user)
    if booking.status != 'PENDING':
        return Response({'error': 'không thể cập nhật.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = BookingCreateSerializer(booking, data=request.data, partial=True)
    if serializer.is_valid():
        room = booking.room_id
        checkin = serializer.validated_data.get('checkin_date', booking.checkin_date)
        checkout = serializer.validated_data.get('checkout_date', booking.checkout_date)
        days = (checkout - checkin).days
        total_price = days * room.price_per_night
        serializer.save(total_price=total_price)
        return Response(
            {'message': 'Cập nhật booking thành công!',
            'data': serializer.data,
            },
            status=status.HTTP_200_OK
            )
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

# CANCEL Booking API View
@csrf_exempt
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def cancel_booking_api(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user_id=request.user)
    if booking.status != 'PENDING':
        return Response({'error': 'không thể hủy bỏ.'}, status=status.HTTP_400_BAD_REQUEST)
    booking.status = 'CANCELLED'
    booking.save()
    return Response({'message': 'Hủy booking thành công'}, status=status.HTTP_200_OK)
    