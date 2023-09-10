from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='id', primary_key=True)


    class Meta:
        managed = True
        db_table = 'Profile'

