# Generated by Django 5.0.6 on 2024-07-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_stripeproduct_shippable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripeproduct',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='stripeproduct',
            name='updated_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
