from django.core.management.base import BaseCommand
from inventory.models import Inventory
import decimal

class Command(BaseCommand):
    help = 'Converts the char values to a decimal'

    def handle(self, *args, **kwargs):
        for item in Inventory.objects.all():
            try:
                item.price = decimal.Decimal(item.price)
                item.save()
            except (ValueError, decimal.InvalidOperation):
                # Handle or log conversion errors
                item.price = None
                item.save()

        self.stdout.write(self.style.SUCCESS('Conversion completed successfully'))
