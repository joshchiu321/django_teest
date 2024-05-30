# comments/forms.py
from django import forms
from bikeStation.models import BikeStationInfo

class StationSelectForm(forms.Form):
    station_no = forms.ModelChoiceField(
        queryset=BikeStationInfo.objects.all(),
        widget=forms.Select(attrs={'class': 'station-select', 'data-autocomplete': 'true'})
    )
