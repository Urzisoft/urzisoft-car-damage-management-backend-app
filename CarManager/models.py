from django.db import models


class CarsReport(models.Model):
    license_plate = models.CharField(max_length=15, default='X')
    image_url = models.ImageField(upload_to='car-manager/data-to-identify')
    damage_severity = models.CharField(max_length=15, blank=True)
    car_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.license_plate
