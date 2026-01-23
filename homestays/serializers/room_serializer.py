
from rest_framework import serializers
from homestays.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_name',
            'description', 
            'max_guests',
            'price_per_night',
            'status'
        ]
        read_only_fields = ['id', 'status']
        