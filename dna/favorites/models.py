
from django.db import models

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Pirate(models.Model):
    name = models.CharField(max_length=125)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name