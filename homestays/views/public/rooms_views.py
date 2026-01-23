
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from homestays.models import Room
from rest_framework.permissions import AllowAny
from homestays.serializers.room_serializer import RoomSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class PublicRoomViewSet(ReadOnlyModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

    # PUBLIC – khách xem phòng
    def get_queryset(self):
        return Room.objects.filter(status=Room.RoomStatus.AVAILABLE)
    
    # khach tim phong
    @action(detail= False, methods= ['get'])
    def available(self, request):
        checkin = request.query_params.get('checkin')
        checkout = request.query_params.get('checkout')
        guests = request.query_params.get('guests')

        rooms = Room.objects.filter(status = Room.RoomStatus.AVAILABLE)

        # loc theo so luong khach 
        if guests: 
            rooms = rooms.filter(max_guests__gte=int(guests)) # gte Greater Than or Equal (lon hon hoac bang)

        # loc theo thoi gian 
        if checkin and checkout:
            try:
                checkin = datetime.strptime(checkin, '%Y-%m-%d').date()
                checkout = datetime.strptime(checkout, '%Y-%m-%d').date()
            except ValueError:
                return Response(
                    {'error': 'Định dạng ngày phải là YYYY-MM-DD'},
                        status= status.HTTP_400_BAD_REQUEST
                )
            rooms = rooms.exclude(  # dùng exclude để lọc bỏ ra những phòng đã được đặt trong khoảng thời gian này, còn filter sẽ lấy những phòng đã được đặt
                booking__status='CONFIRMED',
                booking__checkin_date__lt=checkout,
                booking__checkout_date__gt=checkin
            ).distinct()
        serializer = self.get_serializer(rooms, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
