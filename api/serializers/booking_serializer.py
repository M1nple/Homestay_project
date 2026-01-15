from rest_framework import serializers
from booking.models import Booking

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'checkin_date',
            'checkout_date',
            'guests',
            'created_at'
        ]
    def validate(self, data):
        checkin_date = data.get('checkin_date')
        checkout_date = data.get('checkout_date')
        if checkout_date <= checkin_date:
            raise serializers.ValidationError("Ngày trả phòng phải sau ngày nhận phòng.")
        return data
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
