import requests
from homestays.models import City, District, Ward

url = "https://provinces.open-api.vn/api/?depth=3"
data = requests.get(url).json()

for city_data in data:
    city, _ = City.objects.get_or_create(
        code=city_data['code'],
        defaults={'name': city_data['name']}
    )

    for d in city_data.get('districts', []):
        district, _ = District.objects.get_or_create(
            code=d['code'],
            defaults={
                'name': d['name'],
                'city': city
            }
        )

        for w in d.get('wards', []):
            Ward.objects.get_or_create(
                code=w['code'],
                defaults={
                    'name': w['name'],
                    'district': district
                }
            )
