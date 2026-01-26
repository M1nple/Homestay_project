from django.urls import path, include
from rest_framework.routers import DefaultRouter

from booking.views.customer.booking_views import CustomerBookingViewSet
from booking.views.host.booking_views import HostBookingViewSet


# public router
customer_router = DefaultRouter()
customer_router.register(r'booking', CustomerBookingViewSet, basename= 'customer-booking')

host_router = DefaultRouter()
host_router.register(r'booking', HostBookingViewSet, basename= 'host-booking')

urlpatterns = [ 
    path('customer/', include(customer_router.urls)),
    path('host/', include(host_router.urls))

    # api/customer/booking

]
