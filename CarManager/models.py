from django.db import models


class CarsReport(models.Model):
    image_url = models.ImageField(upload_to='car-manager/data-to-identify')

    def __str__(self):
        return str(self.image_url)
