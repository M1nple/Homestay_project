from django import forms
from homestays.models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [  'room_name', 'description', 'max_guests', 'price_per_night', 'status']
        labels = {
            'room_name': 'Name',
            'description': 'Description',
            'max_guests': 'Max Guests',
            'price_per_night': 'Price per Night',
            'status': 'Room Status',
        }