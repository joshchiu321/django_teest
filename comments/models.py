from django.db import models
from django.utils import timezone
from bikeStation.models import BikeStationInfo
from django.contrib.auth.models import User


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id')
    username = models.TextField()
    station_no = models.ForeignKey(BikeStationInfo, on_delete=models.CASCADE, db_column='station_no')
    create_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)
    comment = models.TextField()
