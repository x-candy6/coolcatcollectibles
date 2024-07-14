from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    item_id = models.AutoField(primary_key=True)
    ebay_itemid = models.CharField(db_column='ebay_itemID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_title = models.CharField(db_column='Listing_Title', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=50, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='publisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    series_name = models.CharField(db_column='Series_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_title = models.CharField(db_column='Full_Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    release_date = models.CharField(db_column='Release_Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    picurl = models.TextField(db_column='PicURL', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    sale = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    time_era = models.CharField(max_length=64, blank=True, null=True)

    #Change to numeric
    #price = models.CharField(db_column='Price', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)


    # Add the following columns: user, booleans for stores(ebay, tiktok, amazon, etsy)

    class Meta:
        managed = True
        db_table = 'inventory'

# Table for viewing all literature actors associated with a single piece(connected to inventory)
class Characters(models.Model):
    character_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    character_name = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'characters'
