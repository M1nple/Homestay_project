from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-wards/', views.load_wards, name='ajax_load_wards'),
    path('host/create/homestay/', views.create_homestay, name='create_homestay'),
    path('host/homestay/update/<int:homestay_id>/', views.update_homestays, name='update_homestays'),
    path('host/homestay/list/', views.host_homestay_list, name='my_homestay'),
    path('host/homestay/delete/image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('homestay/<int:homestay_id>/', views.detail_homestay, name='detail_homestay'),
    ]