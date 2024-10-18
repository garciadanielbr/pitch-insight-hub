from django.core.management.base import BaseCommand
from analytics.services.data_operations import fetch_and_store_teams

class Command(BaseCommand):
    help = 'Fetch teams data from API-Football and store in database'

    def handle(self, *args, **options):
        fetch_and_store_teams()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored teams data'))