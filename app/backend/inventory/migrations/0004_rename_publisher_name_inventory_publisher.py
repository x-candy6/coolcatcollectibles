# Generated by Django 5.0.6 on 2024-06-27 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_comic_id_inventory_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='publisher_name',
            new_name='publisher',
        ),
    ]
