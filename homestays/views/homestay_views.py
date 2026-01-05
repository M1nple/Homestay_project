from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required, host_verified_required
from homestays.models import Homestays, HomestayImage, Room
from homestays.forms import HomestayForm
from django.contrib import messages
from django.contrib.auth import authenticate

# HOME VIEW
def home(request):
    homestays = Homestays.objects.all()
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'base/home.html', {'homestays': homestays})

# HOMESTAY DETAIL VIEW
@login_required(login_url='login')
def detail_homestay(request, homestay_id):
    homestays = Homestays.objects.filter(HomestayID= homestay_id)
    images = HomestayImage.objects.filter(homestay= homestay_id)
    return render(request, 'homestay/detail_homestay.html', {'homestays': homestays, 'images': images})

# HOST HOMESTAY LIST VIEW
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def host_homestay_list(request):
    homestays = Homestays.objects.filter(hostID=request.user)
    rooms = Room.objects.filter(homestay__hostID=request.user)
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'homestay/list_homestay.html', {'homestays': homestays, 'rooms': rooms})

# CREATE HOMESTAY VIEW
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def create_homestay(request):
    if request.method == 'POST':
        form = HomestayForm(request.POST, request.FILES)
        if form.is_valid():
            homestay = form.save(commit=False)
            homestay.hostID = request.user
            homestay.save()

            # Lưu ảnh homestay nếu có
            images = request.FILES.getlist('image')
            for image in images:
                HomestayImage.objects.create(homestay=homestay, image=image)

            messages.success(request, 'Homestay created successfully!')
            return redirect('home')
    else:
        form = HomestayForm()

    return render(request, 'homestay/create_homestay.html', {'form': form})

# UPDATE HOMESTAY VIEW
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def update_homestays(request, homestay_id):
    homestay = get_object_or_404(Homestays, HomestayID=homestay_id, hostID=request.user)
    if request.method == 'POST':
        form = HomestayForm(request.POST, request.FILES, instance=homestay)
        if form.is_valid():
            form.save()

            # Xử lý ảnh homestay
            images = request.FILES.getlist('image')
            for image in images:
                HomestayImage.objects.create(homestay=homestay, image=image)
        messages.success(request, 'Homestay updated successfully!')
        return redirect("my_homestay")
    else:
        form = HomestayForm(instance=homestay)
        context = {
            'form': form,
            'homestay': homestay,
        }
    
    images = HomestayImage.objects.filter(homestay=homestay)
    return render(request, 'homestay/update_homestay.html', {'images': images, **context})

# DELETE IMAGE VIEW
@login_required(login_url='login')
@role_required('HOST')  
@host_verified_required
def delete_image(request, image_id):
    image = get_object_or_404(HomestayImage, id=image_id, homestay__hostID=request.user)
    if request.method == 'POST':
        image.image.delete(save=False)  # Xóa file ảnh khỏi hệ thống lưu trữ
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        # return redirect("homestay/update_homestay.html", homestay_id=image.homestay.HomestayID)
    return redirect(request.META.get('HTTP_REFERER', '/'))
 
# DELETE HOMESTAY VIEW
@login_required(login_url='login')
@role_required('HOST')  
@host_verified_required
def delete_homestay(request, homestay_id):
    homestay = get_object_or_404(Homestays, HomestayID=homestay_id, hostID=request.user)
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(request, username=request.user.username, password=password)
        if user:
            homestay.delete()
            messages.success(request, 'Xóa thành công!')
            return redirect('my_homestay')
        else:
            messages.error(request, 'Sai mật khẩu.')
    # return redirect('my_homestay')
    return render(request, 'homestay/confirm_delete_homestay.html', {'homestay': homestay})   