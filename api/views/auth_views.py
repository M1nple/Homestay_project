from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from homestay_project.accounts.serializer import RegisterSerializer, HostRequestSerializer
from accounts.models import HostRequest
from homestay_project.accounts.permissions import IsAdmin
from django.utils import timezone 

# login API View map thằng TokenObtainPairView của thư viện djangorestframework-simplejwt

# logout API View 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request): # jwt không cần xóa token ở server nên chỉ cần trả về thông báo đăng xuất thành công
    return Response({'message': 'Đăng xuất thành công!'}, status=status.HTTP_200_OK)

# register API View
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message': 'Đăng ký thành công!',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def host_request_api(request):
    serializer =  HostRequestSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message': 'Yêu cầu trở thành host đã được gửi!',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsAdmin])
def approve_host_request_api(request, request_id):
    try:
        host_request = HostRequest.objects.get(id=request_id, status='PENDING')
    except HostRequest.DoesNotExist:
        return Response({'error': 'Yêu cầu không tồn tại hoặc đã được xử lý.'}, status=status.HTTP_404_NOT_FOUND)

    # Tạo HostProfile
    from accounts.models import HostProfile
    HostProfile.objects.create(
        user=host_request.user,
        citizen_id_number=host_request.citizen_id_number,
        address=host_request.address,
        bank_account=host_request.bank_account,
        verified=True
    )

    # Cập nhật trạng thái yêu cầu
    host_request.status = 'APPROVED'
    host_request.reviewed_at = timezone.now()
    host_request.save()

    # Cập nhật role user
    user = host_request.user
    user.role = 'HOST'
    user.save()

    return Response({'message': 'Yêu cầu trở thành host đã được phê duyệt.'}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsAdmin])
def reject_host_request_api(request, request_id):
    try:
        host_request = HostRequest.objects.get(id=request_id, status='PENDING')
    except HostRequest.DoesNotExist:
        return Response({'error': 'Yêu cầu không tồn tại hoặc đã được xử lý.'}, status=status.HTTP_404_NOT_FOUND)

    # Cập nhật trạng thái yêu cầu
    host_request.status = 'REJECTED'
    host_request.reviewed_at = timezone.now()
    host_request.save()

    return Response({'message': 'Yêu cầu trở thành host đã bị từ chối.'}, status=status.HTTP_200_OK)