# Generated by Django 5.0.6 on 2024-07-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_inventory_sale_inventory_time_era_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.DecimalField(blank=True, db_column='Price', decimal_places=2, max_digits=10, null=True),
        ),
    ]
