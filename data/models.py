from django.db import models

# Create your models here.
class House(models.Model):
    houseId = models.IntegerField()
    region = models.CharField(max_length=100)
    type_choices = [
        ('Single', 'Single Family'),
        ('Condo', 'Condo'),
        ('Top', 'Top Tier'),
        ('Middle', 'Middle Tier'),
        ('Bottom', 'Bottom Tier'),
        ('Studio', 'Studio'),
        ('One', 'One Bed'),
        ('Two', 'Two Bed'),
        ('Three', 'Three Bed'),
        ('Four', 'Four Bed'),
        ('Many', 'Many Bed'),
    ]
    HouseType = models.CharField(max_length=100, choices=type_choices)

    def __str__(self):
        return "{} - {} - {}".format(self.houseId, self.region, self.HouseType)

class Price(models.Model):
    priceId = models.IntegerField()
    houseId = models.ForeignKey(House, on_delete=models.CASCADE)
    listingDate = models.DateField(blank=False)
    Price = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.houseId, self.listingDate, self.Price)
    
