from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from homestays.models import Homestays
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from api.serializers.homestay_serializer import HomestaySerializer

from api.permissions import IsHost


# GET All Homestays API View
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_homestays_api(request):
    homestay = Homestays.objects.all()
    serialaizer = HomestaySerializer(homestay, many=True)
    return Response(serialaizer.data, status=status.HTTP_200_OK)

# GET Host Homestays API View
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsHost])
def get_host_homestays_api(request):
    homestays = Homestays.objects.filter(hostID=request.user)
    serializer = HomestaySerializer(homestays, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET Homestay Details API View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_homestay_details_api(request, homestay_id):
    try:
        homestay = Homestays.objects.get(HomestayID=homestay_id)
    except Homestays.DoesNotExist:
        return Response({'error': 'Homestay not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = HomestaySerializer(homestay)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create Homestay API View
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsHost])
def create_homestay_api(request):
        serializer = HomestaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save( hostID=request.user)  
            return Response(
                {
                    'message': 'Homestay created successfully!',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# PUT Update Homestay API View
@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsHost])
def update_homestay_api(request, homestay_id):
    try:
        homestay = Homestays.objects.get(HomestayID=homestay_id, hostID=request.user)
    except Homestays.DoesNotExist:
        return Response({'error': 'Homestay not found.'}, status=status.HTTP_404_NOT_FOUND)
    serialaizer = HomestaySerializer(homestay, data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(
            {
                    'message': 'Homestay updated successfully!',
                    'data': serialaizer.data
                },
                status=status.HTTP_200_OK
            )
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE Homestay API View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsHost])
def delete_homestay_api(request, homestay_id):
    try:
        homestay = Homestays.objects.get(HomestayID=homestay_id, hostID=request.user)
    except Homestays.DoesNotExist:
        return Response({'error': 'Homestay not found.'}, status=status.HTTP_404_NOT_FOUND)
    homestay.delete()
    return Response({'message': 'Homestay deleted successfully!'}, status=status.HTTP_200_OK)