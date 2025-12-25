from accounts.models import User, HostProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from accounts.forms import *
from accounts.forms import HostRequestForm


# Host Registration View

@login_required(login_url='login')
def host_request(request):
    if request.method == 'POST':
        form = HostRequestForm(request.POST)
        if form.is_valid():
            host_request = form.save(commit=False)
            host_request.user = request.user
            host_request.save()
            return HttpResponse('Host Request successful!')
    else:
        form = HostRequestForm()
    return render(request, 'host_request_form.html', {'form': form})