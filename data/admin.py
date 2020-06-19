from django.contrib import admin

# Register your models here.
from .models import House, Price

class HouseAdmin(admin.ModelAdmin):
	list_display = ['houseId', 'region', 'HouseType']

class PriceAdmin(admin.ModelAdmin):
	list_display = ['houseId', 'Price']

admin.site.register(House, HouseAdmin)
admin.site.register(Price, PriceAdmin)