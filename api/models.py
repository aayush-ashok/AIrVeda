from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.
class Device(models.Model):
    uid = models.IntegerField(null=False,primary_key=True)
    name = models.CharField(max_length=200)
    def __int__(self):
        return self.uid
    
class Temperatures(models.Model):
    uid = models.ForeignKey(Device,on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5,decimal_places=2)
    DateTime = models.DateTimeField(default=datetime.now())
    
    def __int__(self):
        return self.uid
    
class Humidity(models.Model):
    uid = models.ForeignKey(Device,on_delete=models.CASCADE)
    humidity = models.DecimalField(max_digits=2,decimal_places=2)
    DateTime = models.DateTimeField(default=datetime.now())
    
    def __int__(self):
        return self.uid
    