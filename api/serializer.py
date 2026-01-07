from rest_framework import serializers
from homestays.models import Homestays, Room

class HomestaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Homestays
        fields = [
            'name', 
            'description', 
            'address', 
            'city', 
            'district', 
            'ward', 
            'price_per_night', 
            'max_guests', 
            'status'
        ]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'room_name',
            'description', 
            'max_guests',
            'price_per_night',
            'status'
        ]