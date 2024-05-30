
from django.core.management.base import BaseCommand
from bikeStation.utils import fetch_and_store_bike_station_status

class Command(BaseCommand):
    help = 'Fetch and store bike station status'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The URL to fetch the JSON data from')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        fetch_and_store_bike_station_status(url)
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored bike station status.'))
