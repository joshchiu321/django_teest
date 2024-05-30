from rest_framework import generics
from .models import BikeStationInfo, BikeStationStatus
from .serializers import BikeStationInfoSerializer, BikeStationStatusSerializer
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import serializers
from rest_framework import viewsets
from django.db.models import Q
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


def search_stations(request):
    query = request.GET.get('q', '')
    area = request.GET.get('area', '')
    stations = []

    if query or area:
        filters = Q()
        if query:
            filters |= Q(station_name__icontains=query) | Q(station_name_en__icontains=query)
        if area:
            filters &= Q(station_area__icontains= area)

        stations = BikeStationInfo.objects.filter(filters)

    return render(request, 'bikeStation/search_station.html', {'stations': stations})