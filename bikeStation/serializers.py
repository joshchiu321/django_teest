from rest_framework import serializers
from .models import BikeStationInfo, BikeStationStatus

class BikeStationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeStationInfo
        fields = '__all__'

class BikeStationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeStationStatus
        fields = '__all__'
