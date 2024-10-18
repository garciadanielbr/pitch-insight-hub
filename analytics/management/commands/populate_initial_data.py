from django.core.management.base import BaseCommand
from analytics.services.data_operations import populate_initial_data

class Command(BaseCommand):
    help = 'Populate initial data for leagues and seasons'

    def handle(self, *args, **options):
        populate_initial_data()
        self.stdout.write(self.style.SUCCESS('Successfully populated initial data'))