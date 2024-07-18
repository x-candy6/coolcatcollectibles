import datetime
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
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True, default=9.99)

    # Stripe Integration
    stripe_product_id = models.ForeignKey('StripeProduct', on_delete=models.CASCADE, blank=True, null=True)
    package_height = models.DecimalField(max_digits=5, decimal_places=2, default=9.0 )
    package_length = models.DecimalField(max_digits=5, decimal_places=2, default=12.0)
    package_width = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    package_weight = models.DecimalField(max_digits=5, decimal_places=2, default = 15.0)

    # Add the following columns: user, booleans for stores(ebay, tiktok, amazon, etsy)

    class Meta:
        managed = True
        db_table = 'inventory'


class StripeProduct(models.Model):
    product_id = models.CharField(primary_key=True, max_length=128)
    item_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming price is stored as DecimalField in Inventory
    currency = models.CharField(max_length=16, default='usd')
    
    description = models.TextField(blank=True, null=True)  
    item_object = models.CharField(max_length=64, default="product", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    shippable = models.BooleanField(null=True)
    tax_code = models.IntegerField(default=99999999, blank=True)

    created_at = models.IntegerField(blank=True)
    updated_at = models.IntegerField(blank=True)
    images = models.CharField(max_length=255)  # Assuming picurl is stored as CharField in Inventory
    url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stripe_product'

    # def save(self, *args, **kwargs):
    #     if isinstance(self.created_at, int):  # Check if created_at is a Unix timestamp
    #         self.created_at = datetime.datetime.fromtimestamp(self.created_at)
    #         self.updated_at = datetime.datetime.fromtimestamp(self.created_at)
    #     super().save(*args, **kwargs)

# Table for viewing all literature actors associated with a single piece(connected to inventory)
class Characters(models.Model):
    character_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    character_name = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'characters'
