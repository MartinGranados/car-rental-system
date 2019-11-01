# Generated by Django 2.2.1 on 2019-11-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_vehicle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='available',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='rented',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='reserved',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Rented', 'Rented'), ('Maintenance', 'Maintenance')], default='Available', max_length=11),
        ),
    ]
