from rest_framework import serializers
from homestays.models import Homestays, Room
from accounts.models import User

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
    def validate(self, data):
        city = data.get('city')
        district = data.get('district')
        ward = data.get('ward')
        if district and district.city != city:
            raise serializers.ValidationError("quận huyện không thuộc thành phố.")
        if ward and ward.district != district:
            raise serializers.ValidationError("xã phường không thuộc quận huyện.")
        return data
            
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username', 'email', 'role'
            'email', 
            'role'
        ]   


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'phone', 
            'role', 
            'is_active', 
            'date_joined', 
            'last_login', 
            'password'
        ]
