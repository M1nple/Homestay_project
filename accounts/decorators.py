from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseForbidden

from accounts.models import HostProfile

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role != role:
                return redirect('home')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def host_verified_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        try:
            host_profile = request.user.host_profile
        except HostProfile.DoesNotExist:
            return redirect('host_request')

        if not host_profile.verified:
            return redirect('host_request')

        return view_func(request, *args, **kwargs)

    return wrapper
