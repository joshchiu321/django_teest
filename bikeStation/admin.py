from django.contrib import admin
from .models import BikeStationInfo, BikeStationStatus

admin.site.register(BikeStationInfo)
admin.site.register(BikeStationStatus)