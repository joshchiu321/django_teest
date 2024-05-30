import requests
from datetime import datetime
from bikeStation.models import BikeStationInfo, BikeStationStatus

def fetch_and_store_bike_station_info(url):
    response = requests.get(url)
    data = response.json()

    for station in data:
        BikeStationInfo.objects.update_or_create(
            station_no=station['sno'],
            defaults={
                'station_name': station['sna'],
                'station_area': station['sarea'],
                'station_address': station['ar'],
                'station_area_en': station['sareaen'],
                'station_name_en': station['snaen'],
                'station_address_en': station['aren'],
                'latitude': station['latitude'],
                'longitude': station['longitude'],
                'act': station['act'],
            }
        )

def fetch_and_store_bike_station_status(url):
    response = requests.get(url)
    data = response.json()

    for station in data:
        station_info = BikeStationInfo.objects.get(station_no=station['sno'])
        BikeStationStatus.objects.update_or_create(
            station_no=station_info,
            mday=datetime.strptime(station['mday'], '%Y-%m-%d %H:%M:%S'),
            defaults={
                'srcUpdateTime': datetime.strptime(station['srcUpdateTime'], '%Y-%m-%d %H:%M:%S'),
                'updateTime': datetime.strptime(station['updateTime'], '%Y-%m-%d %H:%M:%S'),
                'infoTime': datetime.strptime(station['infoTime'], '%Y-%m-%d %H:%M:%S'),
                'infoDate': datetime.strptime(station['infoDate'], '%Y-%m-%d').date(),
                'total': station['total'],
                'available_rent_bikes': station['available_rent_bikes'],
                'available_return_bikes': station['available_return_bikes'],
            }
        )
