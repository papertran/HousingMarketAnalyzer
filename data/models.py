from django.db import models

# Create your models here.
class House(models.Model):
    houseId = models.IntField()
    region = models.CharField()
    HouseType = models.CharField()

class Price(models.Model):
    priceId = models.IntField()
    houseId = models.IntField()
    listingDate = models.DateTime()
    Price = models.IntField()
    
