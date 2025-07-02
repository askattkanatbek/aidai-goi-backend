from django.db import models

class Car(models.Model):
    CLASS_CHOICES = [
        ('economy', 'Эконом'),
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    number_plate = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
