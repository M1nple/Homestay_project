from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # Authentication URLs
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Homestay URLs
    path('homestay/create/', views.create_homestay_api, name='create_homestay_api'),
    path('homestay/', views.get_all_homestays_api, name='get_all_homestays_api'),
    path('homestay/<int:homestay_id>/', views.get_homestay_details_api, name='get_homestay_details_api'),
    path('homestay/update/<int:homestay_id>/', views.update_homestay_api, name='update_homestay_api'),
    path('homestay/delete/<int:homestay_id>/', views.delete_homestay_api, name='delete_homestay_api'),
    # Room URLs
    path('room/create/<int:homestay_id>/', views.create_room_api, name='create_room_api'),
    path('room/', views.get_all_rooms_api, name='get_all_rooms_api'),
    path('room/update/<int:room_id>/', views.update_room_api, name='update_room_api'),
    path('room/delete/<int:room_id>/', views.delete_room_api, name='delete_room_api'),

]



