# api/models.py

from django.db import models

class Product(models.Model):
    ANIMAL_CHOICES = [
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('small_animal', 'Small Animal'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    animal_type = models.CharField(max_length=15, choices=ANIMAL_CHOICES, default='cat')

    def __str__(self):
        return f"{self.name}: {self.price} ({self.animal_type})"
        