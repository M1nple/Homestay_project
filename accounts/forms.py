from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone']



class HostRequestForm(forms.ModelForm):
    class Meta:
        model = HostRequest
        fields = ['citizen_id_number', 'bank_account', 'address', 'note']
        labels = {
            'citizen_id_number': 'Citizen ID Number',
            'bank_account': 'Bank Account',
            'address': 'Address',
            'note': 'Note',
        }


# User Authentication Form (Login)
# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
