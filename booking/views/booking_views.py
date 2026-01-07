from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required, host_verified_required
from booking.models import Booking
from homestays.forms import HomestayForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db.models import Q
# CHECK ROOM AVAILABILITY VIEW
@login_required(login_url='login')
def is_room_available(room, check_in, check_out):
    return not Booking.objects.filter(
        room=room,
        status__in=['pending', 'confirmed'],
        check_in__lt=check_out,
        check_out__gt=check_in
    ).exists()