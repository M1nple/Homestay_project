from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from api.serializers.room_serializer import RoomSerializer
from homestays.models import Room, City, District, Ward
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from api.permissions import IsHost

# POST Create Room API View
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsHost])
def create_room_api(request, homestay_id):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(homestay_id=homestay_id)  
        return Response(
            {
                'message': 'Room created successfully!',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET room by homestay API View
@api_view(['GET'])
@permission_classes([AllowAny])
def get_room_by_homestay_api(request, homestay_id):
    room = Room.objects.filter(homestay_id=homestay_id)
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET Host Rooms API View
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsHost])
def get_host_rooms_api(request):
    rooms = Room.objects.filter(homestay__hostID=request.user)
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# # PUT Update Homestay API View
@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsHost])
def update_room_api(request, room_id):
    try:
        room = Room.objects.get(id=room_id, homestay__hostID=request.user)
    except Room.DoesNotExist:
        return Response({'error': 'Không tìm thấy phòng.'}, status=status.HTTP_404_NOT_FOUND)
    serialaizer = RoomSerializer(room, data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(
            {
                    'message': 'Cập nhật phòng thành công!',
                    'data': serialaizer.data
                },
                status=status.HTTP_200_OK
            )
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# # DELETE Room API View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsHost])
def delete_room_api(request, room_id):
    try:
        room = Room.objects.get(id=room_id, homestay__hostID=request.user)
    except Room.DoesNotExist:
        return Response({'error': 'Không tìm thấy phòng.'}, status=status.HTTP_404_NOT_FOUND)
    room.delete()
    return Response(
        {
            'message': 'Xóa phòng thành công!'
        },
        status=status.HTTP_200_OK
    )

# search room available api view
@api_view(['GET'])
@permission_classes([AllowAny])
def room_available_api(request):
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    guests = request.GET.get('guests')

    rooms = Room.objects.filter(status= Room.RoomStatus.AVAILABLE)

    if guests: 
        rooms = rooms.filter(max_guests__gte=int(guests))
        
    if checkin and checkout:
        checkin = datetime.strptime(checkin, '%Y-%m-%d').date()
        checkout = datetime.strptime(checkout, '%Y-%m-%d').date()
        rooms = rooms.exclude(  # dùng exclude để lọc bỏ ra những phòng đã được đặt trong khoảng thời gian này, còn filter sẽ lấy những phòng đã được đặt
            booking__status='CONFIRMED',
            booking__checkin_date__lt=checkout,
            booking__checkout_date__gt=checkin
        ).distinct()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)