from django.contrib import admin
from .models import Homestays, City, District, Ward, HomestayImage
# Register your models here.
admin.site.register(Homestays),
admin.site.register(City),
admin.site.register(District),
admin.site.register(Ward),
admin.site.register(HomestayImage)
