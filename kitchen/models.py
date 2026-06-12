from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class kitchen(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField(max_length=500, default=None)
    receipe_image = models.ImageField(upload_to='receipe')