from django.utils import timezone
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('HOST', 'Host'),
        ('ADMIN', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')
    phone = models.CharField(max_length=15, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='accounts_user_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_permissions_set',
        blank=True,
    )


class   HostRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='host_requests'
        )
    citizen_id_number = models.CharField(max_length=12)
    bank_account = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=255)
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='PENDING'
        )
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"HostRequest({self.user.username}, {self.status})"


class HostProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='host_profile'
    )
    citizen_id_number = models.CharField(max_length= 12, unique=True)
    bank_account = models.IntegerField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=255)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
