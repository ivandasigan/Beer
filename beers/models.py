from django.db import models

# Create your models here.

class Beer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    srp = models.FloatField()
    
class Brand(models.Model):
