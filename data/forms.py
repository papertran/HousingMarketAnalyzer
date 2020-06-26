from django import forms
from .regionList import regions
class queryForm(forms.Form):
	
	region = forms.ChoiceField(choices=regions)
	type_choices = [
        ('All Homes', 'All Homes'),
        ('Single Family', 'Single Family'),
        ('Condo', 'Condo'),
        ('Top Tier', 'Top Tier'),
        ('Middle Tier', 'Middle Tier'),
        ('Bottom Tier', 'Bottom Tier'),
        ('Studio', 'Studio'),
        ('One Bed', 'One Bed'),
        ('Two Bed', 'Two Bed'),
        ('Three Bed', 'Three Bed'),
        ('Four Four', 'Four Bed'),
        ('Many Four', 'Many Bed'),
    ]
	houseType = forms.ChoiceField(choices= type_choices)
	startDate = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type':'date'}), required=True)
	endDate = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type':'date'}), required=True)

	