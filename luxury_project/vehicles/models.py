from django.db import models
from users.models import CustomUser

class Vehicle(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)  # ✅ image upload

    def __str__(self):
        return f"{self.brand} {self.name} (${self.price})"