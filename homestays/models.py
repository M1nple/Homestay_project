from django.db import models
from accounts.models import User

# Create your models here.
class City(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name

class Ward(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return self.name


class Homestays(models.Model):
    HomestayID = models.AutoField(primary_key=True)
    hostID = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'HOST'}, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.PROTECT) # dùng PROTECT để tránh xóa thành phố nếu có homestay liên quan
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField() # cho sang bang phong
    # total_rooms = models.IntegerField()
    status = models.BooleanField(default=True)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HomestayImage(models.Model):
    homestay = models.ForeignKey(Homestays, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='homestay_project/homestays/media/homestays/images')

    def __str__(self):
        return f"Image for {self.homestay.name}"
    

class Room(models.Model):
    class RoomStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        BOOKED = 'booked', 'Booked'
        MAINTENANCE = 'maintenance', 'Maintenance'
        INACTIVE = 'inactive', 'Inactive'
    id = models.BigAutoField(primary_key=True)
    homestay = models.ForeignKey(Homestays, on_delete=models.CASCADE, related_name='rooms')
    room_name = models.CharField(max_length=100, help_text= "Tên phòng hoặc số phòng (ví dụ: Phòng 101, Phòng Deluxe)")
    price_per_night = models.DecimalField(max_digits=12, decimal_places=2)
    max_guests = models.PositiveIntegerField()
    status = models.CharField(
        max_length=12,
        choices=RoomStatus.choices,
        default=RoomStatus.AVAILABLE,
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_name} - {self.homestay.name}"
    
