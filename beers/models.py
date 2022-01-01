from django.db import models
import os

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
 

class Beer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/%Y/%m/%D/",null=True, blank=True)
    size = models.CharField(max_length=10)
    srp = models.DecimalField(max_digits=5, decimal_places=1)
    stock = models.IntegerField(default=0)
    ratings = models.DecimalField(max_digits=5, decimal_places=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='beers')
    def __str__(self):
        return self.name 

