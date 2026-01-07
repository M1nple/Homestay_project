from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required, host_verified_required
from homestays.models import Homestays, Room
from django.contrib import messages
from homestays.forms import RoomForm
from django.contrib.auth import authenticate

# create room view
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def create_room(request, homestay_id):
    homestay = get_object_or_404(Homestays, HomestayID=homestay_id, hostID=request.user)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.homestay = homestay
            room.save()
            messages.success(request, 'Tạo phòng thành công!')
            return redirect('my_homestay')
    else:
        form = RoomForm()
    return render(request, 'room/create_room.html', {'homestay': homestay , 'form': form})


# update room view
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, homestay__hostID=request.user)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật phòng thành công!')
            return redirect('my_homestay')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room/update_room.html', {'form': form, 'room': room})

# Delete Room View
@login_required(login_url='login')
@role_required('HOST')
@host_verified_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, homestay__hostID=request.user)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Xóa phòng thành công!')
        return redirect('my_homestay')
    return render(request, 'room/confirm_delete_room.html', {'room': room})