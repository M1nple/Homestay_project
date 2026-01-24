from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from accounts.models import HostRequest, HostProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from accounts.permissions import IsAdmin


class AdminViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = HostRequest.objects.all()

    @action(detail= True, methods=['post'], url_path= 'approve')
    @transaction.atomic

    def approve(self, request, pk = None):
        host_request = self.get_object()
        host_request = get_object_or_404(HostRequest, pk = pk, status = 'PENDING')
        
        # tạo hostprofile
        HostProfile.objects.update_or_create(
            user = host_request.user,
            defaults={
                'citizen_id_number' : host_request.citizen_id_number,
                'address' : host_request.address,
                'bank_account':host_request.bank_account,
                'verified':True
            }
        )

        # cập nhật trạng thái yêu cầu
        host_request.status = 'APPROVED'
        host_request.reviewed_at = timezone.now()
        host_request.save()

        # cập nhật role 
        user = host_request.user
        user.role = 'HOST'
        user.save(update_fields=['role'])

        return Response(
            {'message':'Yêu cầu trở thành host đã được phê duyệt'},
            status= status.HTTP_200_OK
        )
    

    @action(detail= True, methods=['post'], url_path= 'reject')
    @transaction.atomic
    def reject(self, request, pk = None):
        # request_id = self.kwargs['request_id']
        host_request = get_object_or_404(HostRequest, pk = pk, status = 'PENDING')

        reason = request.data.get('reason', '').strip()
        if not reason:
            return Response(
                {'error': 'Vui lòng cung cấp lý do từ chối'},
                status=status.HTTP_400_BAD_REQUEST
            )

        host_request.status = 'REJECTED'
        # host_request.reject_reason = reason
        host_request.reviewed_at = timezone.now()
        host_request.save()

        return Response(
            {'message': 'Yêu cầu trở thành host đã bị từ chối'},
            status=status.HTTP_200_OK
        )
