# Generated by Django 5.0.6 on 2024-07-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_stripeproduct_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripeproduct',
            name='created_at',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stripeproduct',
            name='updated_at',
            field=models.IntegerField(blank=True),
        ),
    ]