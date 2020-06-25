from django.db import models

# Create your models here.
class House(models.Model):
    # houseId = models.IntegerField()
    region = models.CharField(max_length=100)
    # type_choices = [
    #     ('All Homes', 'All Homes'),
    #     ('Single Family', 'Single Family'),
    #     ('Condo', 'Condo'),
    #     ('Top Tier', 'Top Tier'),
    #     ('Middle Tier', 'Middle Tier'),
    #     ('Bottom Tier', 'Bottom Tier'),
    #     ('Studio', 'Studio'),
    #     ('One Bed', 'One Bed'),
    #     ('Two Bed', 'Two Bed'),
    #     ('Three Bed', 'Three Bed'),
    #     ('Four Four', 'Four Bed'),
    #     ('Many Four', 'Many Bed'),
    # ]
    # HouseType = models.CharField(max_length=100, choices=type_choices)
    HouseType = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.region, self.HouseType)

class Price(models.Model):
    # priceId = models.IntegerField()
    houseId = models.ForeignKey(House, on_delete=models.CASCADE)
    listingDate = models.DateField(blank=False)
    Price = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.houseId, self.listingDate, self.Price)
    
