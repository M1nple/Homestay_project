from rest_framework import serializers

from homestays.models import HomestayImage, Homestays

class HomestaySerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    ward_name = serializers.CharField(source='ward.name', read_only=True)

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
            'city_name',
            'district_name',
            'ward_name',
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
    



