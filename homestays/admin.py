from django.contrib import admin
from .models import Homestays, City, District, Room, Ward, HomestayImage
# Register your models here.
# admin.site.register(City),
# admin.site.register(District),
# admin.site.register(Ward),
# admin.site.register(Homestays),
# admin.site.register(HomestayImage)

admin.site.site_header = "  Homestay Admin"
admin.site.index_title = "Admin Dashboard"
admin.site.site_title = "Homestay Admin Portal"

@admin.register(Homestays)
class HomestaysAdmin(admin.ModelAdmin):
    list_display = (
        'HomestayID',
        'hostID',
        'name',
        'city',
        'district',
        'ward', 
        'address', 
        'price_per_night', 
        'crated_at',
        'status',
    )
    search_fields = (
        'name', 
        'hostID__username', 
        'city__name', ''
        'district__name', 
        'ward__name', 
        'address'
    )
    list_filter = (
        'status',

)
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'homestay',
        'room_name',
        'max_guests',
        'status',
    )
    search_fields = (
        'room_name',
        'homestay__name',
    )
    list_filter = (
        'status',
        'homestay',
    )