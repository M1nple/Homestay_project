from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('customer/page/', views.test_customer_page, name='customer_page'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-wards/', views.load_wards, name='ajax_load_wards'),
    path('host/homestay/', views.list_homestays, name='list_homestays'),
    path('host/create/homestay/', views.create_homestay, name='create_homestay'),
    path('host/homestay/list/', views.host_homestay_list, name='my_homestay'),
    path('homestay/<int:homestay_id>/', views.detail_homestay, name='detail_homestay'),
    ]