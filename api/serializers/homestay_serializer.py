from rest_framework import serializers

from homestays.models import HomestayImage, Homestays

class HomestaySerializer(serializers.ModelSerializer):
    # images = serializers.ListField(
    #     child =serializers.ImageField(),
    #     write_only=True,
    #     required=False
    # )

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
            # 'images'
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
    
    # def create(self, validated_data):
    #     images = validated_data.pop('images', [])
    #     homestay = Homestays.objects.create(**validated_data)
    #     for image in images:
    #         HomestayImage.objects.create(homestay=homestay, image=image)
    #     return homestay
            