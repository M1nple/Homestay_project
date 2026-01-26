from django.contrib import admin
from .models import *

from django.utils import timezone
from .models import User

# Register your models here.
admin.site.site_header = "Homestay Admin"
admin.site.index_title = "Admin Dashboard"
admin.site.site_title = "Homestay Admin Portal"
# admin.site.register(User)
# admin.site.register(HostProfile)
# admin.site.register(HostRequest)



@admin.action(description="Approve selected host requests")
def approve_host_request(modeladmin, request, queryset):
    for host_request in queryset:
        if host_request.status != 'PENDING':
            continue

        user = host_request.user

        # Nếu đã là host thì bỏ qua
        if hasattr(user, 'host_profile'):
            continue

        # Tạo HostProfile
        HostProfile.objects.create(
            user=user,
            citizen_id_number=host_request.citizen_id_number,
            address=host_request.address,
            bank_account=host_request.bank_account,
            verified=True
        )

        # Cập nhật role user
        user.role = 'HOST'
        user.save()

        # Update request
        host_request.status = 'APPROVED'
        host_request.reviewed_at = timezone.now()
        host_request.save()

@admin.action(description="Reject selected host requests")
def reject_host_request(modeladmin, request, queryset):
    for host_request in queryset:
        if host_request.status != 'PENDING':
            continue

        host_request.status = 'REJECTED'
        host_request.reviewed_at = timezone.now()
        host_request.save()


@admin.register(HostRequest)
class HostRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'citizen_id_number',
        'status',
        'created_at',
        'reviewed_at'
    )
    list_filter = ('status',)
    search_fields = ('user__username', 'citizen_id_number')
    actions = [approve_host_request, reject_host_request]


@admin.register(HostProfile)
class HostProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'citizen_id_number',
        'verified',
        'created_at'
    )
    search_fields = ('user__username', 'citizen_id_number')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'is_active',
        'is_staff',
        'date_joined'
    )
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active', 'is_staff')