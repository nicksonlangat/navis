# Generated by Django 4.2.4 on 2023-09-05 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.location'),
        ),
    ]