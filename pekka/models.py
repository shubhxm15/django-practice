from django.db import models

class car(models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
