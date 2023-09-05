# Generated by Django 4.2.4 on 2023-08-24 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='destination',
        ),
        migrations.AddField(
            model_name='shipment',
            name='route_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='route_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='core.location'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
    ]
