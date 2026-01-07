from accounts.models import User, HostProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from accounts.forms import *


# User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Đăng ký thành công! Vui lòng đăng nhập."))
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register_form.html', {'form': form})
        

# User Authentication View (Login)
def login_view(request): # không để login, logout vì trùng với hàm login của django
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in.')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, ("Login thành công "))
                return redirect('home')
            else:
                messages.error(request, ("sai tài khoản hoặc mật khẩu "))
                return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    auth_logout(request)   #  logout là thư viện đã import 
    messages.success(request, ("logout thành công "))
    return redirect('home')


@login_required(login_url='login')
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    me = request.user
    try:
        user_profile = HostProfile.objects.get(user=me)
    except HostProfile.DoesNotExist:
        user_profile = None

    context = {
        'user': me,
        'user_profile': user_profile,
    }
    return render(request, 'home.html', context)