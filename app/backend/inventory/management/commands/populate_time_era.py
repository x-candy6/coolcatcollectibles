from django.core.management.base import BaseCommand
from inventory.models import Inventory

class Command(BaseCommand):
    help = 'Populates the time_era field based on the year field'

    def handle(self, *args, **kwargs):
        for obj in Inventory.objects.all():
            if obj.year:
                if 1938 <= obj.year <= 1956:
                    obj.time_era = 'Golden'
                elif 1956 <= obj.year <= 1970:
                    obj.time_era = 'Silver'
                elif 1970 <= obj.year <= 1985:
                    obj.time_era = 'Bronze'
                elif obj.year >= 1985:
                    obj.time_era = 'Modern'
                else:
                    obj.time_era = None  # Handle any other cases here if needed
                obj.save()
                self.stdout.write(self.style.SUCCESS(f'Updated {obj}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipped {obj} because year is null'))
