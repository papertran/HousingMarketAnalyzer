from django.db import models

# Create your models here.
class House(models.Model):
    transDate = models.FloatField()
    houseAge = models.FloatField()
    distToNearStation = models.FloatField()
    numStore = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.FloatField()
	predicted = models.BooleanField()
    