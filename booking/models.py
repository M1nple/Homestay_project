from django.db import models

class Booking(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    room = models.ForeignKey('homestays.Room', on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    START_CHOICES = (
        ('PENDING', 'Chờ xác nhận'),
        ('CONFIRMED', 'Đã xác nhận'),
        ('CANCELLED', 'Đã hủy'),
    )
    status = models.CharField(max_length=20, choices=START_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    cancelled_at = models.DateTimeField(null= True, blank= True)
    confirm_at =  models.DateTimeField(null= True, blank= True)
