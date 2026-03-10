from atexit import register
from urllib import request
from django.db import router
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from rest_framework.routers import DefaultRouter
from accounts.views.auth_views import AuthViewSet, HostRequestViewSet, MeView
from accounts.views.admin_views import AdminViewSet, UserViewSet



router = DefaultRouter()
router.register(r'register', AuthViewSet, basename='register')

host_router = DefaultRouter()
host_router.register(r'request', HostRequestViewSet, basename= 'host-request')

admin_router = DefaultRouter()
admin_router.register(r'host-requests', AdminViewSet, basename= 'admin')
admin_router.register(r'user', UserViewSet, basename= 'admin-user')

urlpatterns = [
    path('auth/', include(router.urls)),
    path('host/', include(host_router.urls)),
    path('admin/', include(admin_router.urls)),
    path('auth/me/', MeView.as_view(), name='me'),
    
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),

]   