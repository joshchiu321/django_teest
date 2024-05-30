from django.urls import path
from .views import stations_with_no_bikes,no_bikes_view


urlpatterns = [
    path('no-bikes/', no_bikes_view, name='no-bikes'),
    path('api/stations_with_no_bikes/', stations_with_no_bikes, name='stations_with_no_bikes'),

]
