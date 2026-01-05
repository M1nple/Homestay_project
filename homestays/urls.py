from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-wards/', views.load_wards, name='ajax_load_wards'),
    # 
    path('host/homestay/create/', views.create_homestay, name='create_homestay'),
    path('host/homestay/update/<int:homestay_id>/', views.update_homestays, name='update_homestays'),
    path('host/homestay/', views.host_homestay_list, name='my_homestay'),
    path('host/homestay/delete/image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('host/homestay/delete/<int:homestay_id>/', views.delete_homestay, name='delete_homestay'),
    path('host/room/create/<int:homestay_id>/', views.create_room, name='create_room'),
    path('host/room/update/<int:room_id>/', views.update_room, name='update_room'),
    path('host/room/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    # 
    path('homestay/<int:homestay_id>/', views.detail_homestay, name='detail_homestay'),
    ]