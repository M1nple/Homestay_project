# Register your models here.
from django.contrib import admin
from .models import Booking

admin.site.site_header = "  Homestay Admin"
admin.site.index_title = "Admin Dashboard"
admin.site.site_title = "Homestay Admin Portal"
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'checkin_date',
        'checkout_date',
        'guests',
        'total_price',
        'created_at',
        'status',
    )
    search_fields = (
    )
    list_filter = ("status",
    )