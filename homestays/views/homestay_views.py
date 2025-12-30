from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required, host_verified_required
from homestays.models import Homestays, HomestayImage
from homestays.forms import HomestayForm
from django.contrib import messages

# Create your views here.
def home(request):
    homestays = Homestays.objects.all()
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'home.html', {'homestays': homestays})

login_required(login_url='login')
def detail_homestay(request, homestay_id):
    # homestay = Homestays.objects.get(HomestayID=homestay_id)
    homestays = Homestays.objects.filter(HomestayID= homestay_id)
    images = HomestayImage.objects.filter(homestay= homestay_id)
    return render(request, 'homestay/detail_homestay.html', {'homestays': homestays, 'images': images})

@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def host_homestay_list(request):
    homestays = Homestays.objects.filter(hostID=request.user)
    for homestay in homestays:
        homestay.thumbnail = homestay.images.first()
    return render(request, 'homestay/list_homestay.html', {'homestays': homestays})

@login_required(login_url='login')
@role_required('CUSTOMER')  
# @host_verified_required
def test_customer_page(request):
    if request.method == 'POST':
        # Xử lý logic tạo homestay ở đây
        return HttpResponse("customer page ")
    return render(request, 'customer_page.html')

@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def list_homestays(request):
    if request.method == 'POST':
        me = request.user
        homestays = Homestays.objects.filter(hostID=me)
        return render(request, 'host/homestay_list.html', {'homestays': homestays})
    return render(request, 'Host_page.html')



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

