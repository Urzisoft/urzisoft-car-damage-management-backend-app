from django.db import models


class CarsReport(models.Model):
    license_plate = models.CharField(max_length=15, default='X', unique=True)
    image_url = models.ImageField(upload_to='car-manager/data-to-identify')
    damage_severity = models.CharField(max_length=15, blank=True)
    car_entry_date = models.DateTimeField(auto_now_add=True)
    car_leave_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.license_plate
