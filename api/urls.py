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
    path('homestay/host/', views.get_host_homestays_api, name='get_host_homestays_api'),
    # Room URLs
    path('room/create/<int:homestay_id>/', views.create_room_api, name='create_room_api'),
    path('room/', views.get_all_rooms_api, name='get_all_rooms_api'),
    path('room/host/', views.get_host_rooms_api, name='get_host_rooms_api'),
    path('room/update/<int:room_id>/', views.update_room_api, name='update_room_api'),
    path('room/delete/<int:room_id>/', views.delete_room_api, name='delete_room_api'),

    # User URLs
    path('users/', views.list_users_api, name='list_users_api'),
    path('users/<int:user_id>/', views.user_detail_api, name='user_detail_api'),
    path('users/update/<int:user_id>/', views.update_user_api, name='update_user_api'),
    path('users/delete/<int:user_id>/', views.delete_user_api, name='delete_user_api'),

    # Booking URLs
    path('booking/<int:room_id>/create/', views.create_booking_api, name='create_booking_api'),
    path('booking/', views.get_all_bookings_api, name='get_all_bookings_api'),
    path('booking/customer/', views.get_customer_bookings_api, name='get_customer_bookings_api'),
    path('booking/update/<int:booking_id>/', views.update_booking_api, name='update_booking_api'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking_api, name='cancel_booking_api'),
    # Booking management by Host
    path('booking/<int:booking_id>/accept/', views.accept_booking_api, name='accept_booking_api'),
    path('booking/<int:booking_id>/reject/', views.reject_booking_api, name='reject_booking_api'),
]



