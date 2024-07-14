# Generated by Django 5.0.6 on 2024-07-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_guestcart_guestcartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='access_token',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
