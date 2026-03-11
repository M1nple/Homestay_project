from rest_framework.views import APIView
from rest_framework.response import Response
from homestays.models import City
from homestays.serializers.locations_serializer import CitySerializer


class LocationView(APIView):

    def get(self, request):

        cities = City.objects.prefetch_related(
            "districts__wards"
        )

        serializer = CitySerializer(cities, many=True)

        return Response(serializer.data)