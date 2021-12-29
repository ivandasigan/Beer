from django.db import models
import os

from django.db.models.fields import UUIDField
# Create your models here.
import uuid

def filePath(instance, filename):
    # ext = filename.split('.')[-1]
    # filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'media/images/{0}/'.format(filename)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
 

class Beer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    size = models.CharField(max_length=10)
    srp = models.FloatField()
    stock = models.IntegerField(default=0)
    ratings = models.FloatField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='beers')
    def __str__(self):
        return self.name 


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField('images/',null=True)