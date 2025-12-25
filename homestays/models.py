from django.db import models
from accounts.models import User

# Create your models here.
class Homestays(models.Model):
    HomestayID = models.AutoField(primary_key=True)
    hostID = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'HOST'}, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField()
    status = models.BooleanField(default=True)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name