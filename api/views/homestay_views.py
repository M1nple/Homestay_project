from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from api.serializer import HomestaySerializer
from homestays.models import Homestays
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create Homestay API View
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
    

# GET All Homestays API View
@api_view(['GET'])
def get_all_homestays_api(request):
    homestay = Homestays.objects.all()
    serialaizer = HomestaySerializer(homestay, many=True)
    return Response(serialaizer.data, status=status.HTTP_200_OK)

# GET Homestay Details API View
@api_view(['GET'])
def get_homestay_details_api(request, homestay_id):
    try:
        homestay = Homestays.objects.get(HomestayID=homestay_id)
    except Homestays.DoesNotExist:
        return Response({'error': 'Homestay not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = HomestaySerializer(homestay)
    return Response(serializer.data, status=status.HTTP_200_OK)

# PUT Update Homestay API View
@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete_homestay_api(request, homestay_id):
    try:
        homestay = Homestays.objects.get(HomestayID=homestay_id, hostID=request.user)
    except Homestays.DoesNotExist:
        return Response({'error': 'Homestay not found.'}, status=status.HTTP_404_NOT_FOUND)
    homestay.delete()
    return Response({'message': 'Homestay deleted successfully!'}, status=status.HTTP_200_OK)