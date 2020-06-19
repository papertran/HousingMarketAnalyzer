from django.db import models

# Create your models here.
class House(models.Model):
    houseId = models.IntegerField()
    region = models.CharField(max_length=100)
    HouseType = models.CharField(max_length=100)

class Price(models.Model):
    priceId = models.IntegerField()
    houseId = models.IntegerField()
    listingDate = models.DateTimeField()
    Price = models.IntegerField()
    
