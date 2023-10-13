from django.db import models


class Car(models.Model):
    image_url = models.ImageField(upload_to='car-manager/data-to-identify')

    def __str__(self):
        return self.image_url
