from rest_framework import generics
from .models import BikeStationInfo, BikeStationStatus
from .serializers import BikeStationInfoSerializer, BikeStationStatusSerializer
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import serializers
from rest_framework import viewsets

class BikeStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BikeStationInfo.objects.all()
    serializer_class = serializers
def stations_with_no_bikes(request):
    no_bikes_stations = BikeStationStatus.objects.filter(available_rent_bikes=0)
    results = []
    for status in no_bikes_stations:
        results.append({
            'station_no': status.station_no.station_no,
            'station_name': status.station_no.station_name,
        })
    return JsonResponse(results, safe=False)

def no_bikes_view(request):
    return render(request, 'bikeStation/no_bikes.html')


