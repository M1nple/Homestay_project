from django import forms
from homestays.models import Homestays, City, District, Ward

class HomestayForm(forms.ModelForm):
    class Meta:
        model = Homestays
        fields = ['name', 'description', 'address', 'city', 'district', 'ward', 'price_per_night', 'max_guests', 'status']
        labels = {
            'name': 'Homestay Name',
            'description': 'Description',
            'address': 'Address',
            'city': 'City',
            'district': 'District',
            'ward': 'Ward',
            'price_per_night': 'Price per Night',
            'max_guests': 'Maximum Guests',
            'status': 'Available Status',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['district'].queryset = District.objects.none()
        self.fields['ward'].queryset = Ward.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['district'].queryset = District.objects.filter(city_id=city_id)
            except (ValueError, TypeError):
                pass

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['ward'].queryset = Ward.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass
