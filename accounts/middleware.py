from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

class RoleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if request.path.startswith('/admin'):
            return self.get_response(request)

        if not user.is_authenticated:
            return self.get_response(request)

        # CUSTOMER
        if user.role == 'CUSTOMER':
            if request.path.startswith('/host'):
                return redirect('home')

        return self.get_response(request)
