from django.contrib import admin
from .models import Tours, TravelCompanies, Hotels, Countries, Flights, Airlines


admin.site.register(Countries)
admin.site.register(Tours)
admin.site.register(Hotels)
admin.site.register(TravelCompanies)
admin.site.register(Flights)
admin.site.register(Airlines)
