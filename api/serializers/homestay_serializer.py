from rest_framework import serializers
from homestays.models import Homestays

class HomestaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Homestays
        fields = [
            'HomestayID',
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
            