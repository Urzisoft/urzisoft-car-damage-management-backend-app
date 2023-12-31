# Generated by Django 3.2.22 on 2023-10-14 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CarManager', '0004_auto_20231014_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carsreport',
            old_name='car_added',
            new_name='car_entry_date',
        ),
        migrations.AddField(
            model_name='carsreport',
            name='car_leave_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carsreport',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carsreport',
            name='license_plate',
            field=models.CharField(default='X', max_length=15),
        ),
    ]
