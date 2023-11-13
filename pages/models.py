from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)