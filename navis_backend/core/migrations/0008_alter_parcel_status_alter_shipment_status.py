# Generated by Django 4.2.4 on 2023-09-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_client_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='status',
            field=models.CharField(choices=[('READY', 'Ready'), ('DELAYED', 'Delayed'), ('ON WAY', 'On way'), ('ARRIVED', 'Arrived')], default='READY', max_length=255),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('READY', 'Ready'), ('DELAYED', 'Delayed'), ('ON WAY', 'On way'), ('ARRIVED', 'Arrived')], default='READY', max_length=255),
        ),
    ]
