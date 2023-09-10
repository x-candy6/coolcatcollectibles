from django.db import models
from django.conf import settings
# Create your models here.

class Product(models.Model):
    product_id = models.BigAutoField(db_column='product_id', primary_key=True)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    series_name = models.CharField(db_column='Series_Name', max_length=128, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    full_title = models.CharField(db_column='Full_Title', max_length=256, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    release_date = models.CharField(db_column='Release_Date', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    in_collection = models.IntegerField(db_column='In_Collection', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.CharField(db_column='Notes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=50, blank=True, null=True)  # Field name made lowercase.
    picurl = models.CharField(db_column='PicURL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    listing_title = models.CharField(db_column='Listing_Title', max_length=128, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'product'


class Cart(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='id', primary_key=True)
    cartItems = models.ManyToManyField('Product', related_name='carts')


    class Meta:
        managed = True
        db_table = 'Cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'CartItem'
        
    def __str__(self):
        return f"{self.quantity} x {self.product.full_title}"

