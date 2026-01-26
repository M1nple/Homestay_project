from rest_framework import serializers
from booking.models import Booking

class CustomerBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'room',
            'checkin_date',
            'checkout_date',
            'guests',
            'created_at',
            'status'
        ]

    def validate(self, data):
        checkin = data.get('checkin_date')
        checkout = data.get('checkout_date')
        guests = data.get('guests')
        room = data['room']

        # kiểm tra ngày nhận và ngày trả
        if checkin and checkout and checkout <= checkin:
            raise serializers.ValidationError("Ngày trả phòng phải sau ngày nhận phòng.")
        
        # kiểm tra số lượng khách
        if guests and guests > room.max_guests:
            raise serializers.ValidationError(f"Số lượng khách vượt quá sức chứa tối đa của phòng ({room.max_guests} khách).")
        
        # kiểm tra trùng lịch đặt phòng
        if checkin and checkout:
            conflict  = Booking.objects.filter( 
                room=room,
                status__in=['CONFIRMED'],
                checkin_date__lt=checkout, # LT = less than (<) 
                checkout_date__gt=checkin # GT = greater than (>) kiểm tra giao nhau của hai khoảng thời gian với nhau trong database và yêu cầu mới tạo
            ).exists()
            if conflict:
                raise serializers.ValidationError("Phòng đã được đặt trong khoảng thời gian này.")
        return data
    
    def create(self, validated_data):
        user = self.context['request'].user
        room = validated_data['room']
        days = (validated_data['checkout_date'] - validated_data['checkin_date']).days
        total_price = days * room.price_per_night
        return Booking.objects.create(user = user, total_price=total_price, **validated_data)
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
