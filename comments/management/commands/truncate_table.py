from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Truncate data in a specified table'

    def add_arguments(self, parser):
        parser.add_argument('table_name', type=str, help='The name of the table to truncate')

    def handle(self, *args, **options):
        table_name = options['table_name']
        db_engine = settings.DATABASES['default']['ENGINE']

        with connection.cursor() as cursor:
            if 'sqlite' in db_engine:
                cursor.execute(f"DELETE FROM {table_name}")
            elif 'postgresql' in db_engine:
                cursor.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE")
            elif 'mysql' in db_engine:
                cursor.execute(f"TRUNCATE TABLE {table_name}")
            else:
                self.stdout.write(self.style.ERROR('Unsupported database backend'))
                return

        self.stdout.write(self.style.SUCCESS(f'Successfully truncated {table_name}'))
