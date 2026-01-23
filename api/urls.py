from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from api.views.room_views import HostRoomViewSet, PublicRoomViewSet


# public router 
# public_router = DefaultRouter()
# public_router.register(r'rooms', PublicRoomViewSet, basename= 'public-rooms')


# # host router
# host_router = DefaultRouter()
# host_router.register(r'rooms', HostRoomViewSet, basename= 'host-rooms' )

# urlpatterns = [ 
    # auth
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('refresh/', TokenRefreshView.as_view(), name='refresh'),
#     path('auth/logout/', views.logout_api, name='logout_api'),
#     path('auth/register/', views.register_api, name='register_api'),
#     path('auth/host/request/', views.host_request_api, name='host_request_api'),


# PUBLIC
    # path('', include(public_router.urls)),
# HOST
    # path('host/', include(host_router.urls)),
# ]
