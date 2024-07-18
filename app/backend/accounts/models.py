import secrets
from django.db import models
from django.contrib.auth.models import User
from inventory.models import Inventory


# Create your models here.
class Profile(models.Model):
    id = models.OneToOneField(User, models.DO_NOTHING, db_column='id', primary_key=True)
    appid = models.CharField(db_column='AppID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certid = models.CharField(db_column='CertID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runame = models.CharField(db_column='RuName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    oauth_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    authnauth = models.TextField(blank=True, null=True)

    mailing_address = models.TextField(blank=True, null=True, verbose_name='Mailing Address')
    billing_address = models.TextField(blank=True, null=True, verbose_name='Billing Address')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number')

    class Meta:
        managed = True
        db_table = 'profile'



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    mailing_service = models.CharField(max_length=100)
    tracking_id = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'orders'

class UserCart(models.Model):
    user_cart_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user_cart'

class UserCartItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_cart_id = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user_cart_items'

class GuestCart(models.Model):
    guest_cart_id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey('Session', models.DO_NOTHING, to_field='sessionid')

    class Meta:
        managed = True
        db_table = 'guest_cart'


class GuestCartItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    qty = models.IntegerField(blank=True, null=True)
    guest_cart_id = models.ForeignKey(GuestCart, models.DO_NOTHING)
    product_id = models.ForeignKey(Inventory, models.DO_NOTHING)
    session_id = models.ForeignKey('Session', models.DO_NOTHING, to_field='sessionid')

    class Meta:
        managed = True
        db_table = 'guest_cart_items'

class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    sessionid = models.CharField(db_column='sessionID', unique=True, max_length=64)  # Field name made lowercase.
    expire_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    access_token = models.CharField(max_length=512, blank=True, null=True)
    refresh_token = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'session'

    def save(self, *args, **kwargs):
        if not self.sessionid:
            self.sessionid = secrets.token_hex(32)
        super(Session, self).save(*args, **kwargs)



class Wishlist(models.Model):
    product_id = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField()

    class Meta:
        managed = True
        db_table = 'wishlist'