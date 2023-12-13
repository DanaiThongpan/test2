from django.db import models

# Create your models here.
class db(models.Model):
    idc = models.CharField(max_length=10)
    name = models.CharField(max_length=100)