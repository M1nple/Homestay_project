from atexit import register
from urllib import request
from django.db import router
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from rest_framework.routers import DefaultRouter
from accounts.views.auth_views import AuthViewSet, HostRequestViewSet
from accounts.views.admin_views import AdminViewSet, UserViewSet



router = DefaultRouter()
router.register(r'register', AuthViewSet, basename='register')

request_router = DefaultRouter()
request_router.register(r'request', HostRequestViewSet, basename= 'host-request')

admin_router = DefaultRouter()
admin_router.register(r'host-requests', AdminViewSet, basename= 'admin')
admin_router.register(r'user', UserViewSet, basename= 'admin-user')

urlpatterns = [
    path('', include(router.urls)),
    path('host/', include(request_router.urls)),
    path('admin/', include(admin_router.urls)),
    
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),


    # Password reset URLs for built-in views
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
        path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]   