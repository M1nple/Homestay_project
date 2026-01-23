from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.public.rooms_views import PublicRoomViewSet
from .views.host.rooms_views import HostRoomViewSet
from .views.host.homestay_views import HostHomestayViewSet

# public router
public_router = DefaultRouter()
public_router.register(r'rooms', PublicRoomViewSet, basename= 'public-rooms')

# host router
host_router = DefaultRouter()
host_router.register(r'rooms', HostRoomViewSet, basename= 'host-rooms')
host_router.register(r'homestays',HostHomestayViewSet, basename= 'host-homestays' )

urlpatterns = [
    # 
    path('', include(public_router.urls)),

    # 
    path('host/', include(host_router.urls)),

    # create room
    path('host/homestays/<int:homestay_id>/rooms/', 
        HostRoomViewSet.as_view({'post':'create'}), 
        name= 'host-create-room'
        ),

]
