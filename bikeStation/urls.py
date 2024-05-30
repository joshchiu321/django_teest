from django.urls import path
from .views import stations_with_no_bikes,no_bikes_view,search_stations


urlpatterns = [
    path('no-bikes/', no_bikes_view, name='no-bikes'),
    path('data/stations_with_no_bikes_data/', stations_with_no_bikes, name='stations_with_no_bikes'),
    path('search/', search_stations, name='search_stations')
]
