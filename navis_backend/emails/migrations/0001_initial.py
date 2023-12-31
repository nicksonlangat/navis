# Generated by Django 4.2.4 on 2023-08-22 16:38

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('READY', 'Ready'), ('SENDING', 'Sending'), ('SENT', 'Sent'), ('FAILED', 'Failed')], db_index=True, default='READY', max_length=255)),
                ('to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('html', models.TextField()),
                ('plain_text', models.TextField()),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
