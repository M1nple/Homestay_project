from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.serializers.user_serializer import UserSerializer, UserDetailSerializer
from accounts.models import User
from homestay_project.accounts.permissions import IsAdmin

# GET List Users API View
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def list_users_api(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET User Detail API View
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def user_detail_api(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Người dùng không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# PUT Update User API View
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_user_api(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Người dùng không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserDetailSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE User API View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdmin])
def delete_user_api(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Người dùng không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(
        {
            'message': 'Người dùng đã được xóa thành công!'
        },
        status=status.HTTP_200_OK
    )