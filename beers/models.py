from django.db import models

# Create your models here.

class Beer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    srp = models.FloatField()
    def __str__(self):
        return self.name

class Brand(models.Model):
  
    name = models.CharField(max_length=50)
    beers = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
 
