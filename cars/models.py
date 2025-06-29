
from django.db import models

class Car(models.Model):
    CLASS_CHOICES = [
        ('econom', 'Econom'),
        ('comfort', 'Comfort'),
        ('business', 'Business'),
    ]
    model = models.CharField(max_length=100)
    car_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    fuel_level = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    tariff = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.model} ({self.license_plate})"
