# Generated by Django 5.0.6 on 2024-07-14 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_guestcart_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestcartitems',
            name='session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.session', to_field='sessionid'),
        ),
    ]
