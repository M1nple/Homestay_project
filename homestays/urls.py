from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.public.rooms_views import PublicRoomViewSet
from .views.public.homestay_views import PublicHomestayViewSet
from .views.host.rooms_views import HostRoomViewSet
from .views.host.homestay_views import HostHomestayViewSet, HostHomestayImageViewSet


# public router
public_router = DefaultRouter()
public_router.register(r'rooms', PublicRoomViewSet, basename= 'public-rooms')
public_router.register(r'homestays', PublicHomestayViewSet, basename= 'public-homestays')

# host router
host_router = DefaultRouter()
host_router.register(r'rooms', HostRoomViewSet, basename= 'host-rooms')
host_router.register(r'homestays',HostHomestayViewSet, basename= 'host-homestays' )
host_router.register(r'images',HostHomestayImageViewSet, basename= 'host-homestays-image' )

urlpatterns = [ 
    # Public
    path('', include(public_router.urls)),

    # Host
    path('host/', include(host_router.urls)),

    # Host create room
    path('host/homestays/<int:homestay_id>/rooms/', 
        HostRoomViewSet.as_view({'post':'create'}), 
        name= 'host-create-room'
        ),

]
