from rest_framework import serializers
from homestays.models import City, District, Ward


class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = ["id", "name"]


class DistrictSerializer(serializers.ModelSerializer):

    wards = WardSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ["id", "name", "wards"]


class CitySerializer(serializers.ModelSerializer):

    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ["id", "name", "districts"]