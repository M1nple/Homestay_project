from django.http import JsonResponse
from homestays.models import District, City, Ward

# homestays/views.py

def load_districts(request):
    city_id = request.GET.get('city')
    districts = District.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse(list(districts), safe=False)

def load_wards(request):
    district_id = request.GET.get('district')
    wards = Ward.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(wards), safe=False)
