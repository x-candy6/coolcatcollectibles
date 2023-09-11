from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL,
                           models.DO_NOTHING, db_column='id', primary_key=True)
    street_address = models.CharField(
        max_length=255, verbose_name="Street Address")
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=2, verbose_name="State", help_text="Two-letter state abbreviation")
    zip_code = models.CharField(max_length=10, verbose_name="ZIP Code")

    class Meta:
        managed = True
        db_table = 'Profile'

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"
