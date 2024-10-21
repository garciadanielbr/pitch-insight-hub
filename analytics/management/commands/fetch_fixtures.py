from django.core.management.base import BaseCommand
from analytics.services.data_operations import fetch_and_store_fixtures

class Command(BaseCommand):
    help = 'Fetch fixtures data from API-Football and store in database'

    def handle(self, *args, **options):
        message = fetch_and_store_fixtures()
        self.stdout.write(self.style.SUCCESS(message))