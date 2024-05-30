from django.db import models

class BikeStationInfo(models.Model):
    station_no = models.CharField(max_length=15, primary_key=True)
    station_name = models.CharField(max_length=500)
    station_area = models.CharField(max_length=500)
    station_address = models.CharField(max_length=500)
    station_area_en = models.CharField(max_length=500)
    station_name_en = models.CharField(max_length=500)
    station_address_en = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    act = models.CharField(max_length=1)

    def __str__(self):
        return self.station_name

class BikeStationStatus(models.Model):
    station_no = models.ForeignKey(BikeStationInfo, on_delete=models.CASCADE)
    mday = models.DateTimeField()
    srcUpdateTime = models.DateTimeField()
    updateTime = models.DateTimeField()
    infoTime = models.DateTimeField()
    infoDate = models.DateField()
    total = models.IntegerField()
    available_rent_bikes = models.IntegerField()
    available_return_bikes = models.IntegerField()

    def __str__(self):
        return f"{self.station_no} status on {self.infoDate}"
