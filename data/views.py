from django.shortcuts import render
from django.db import connection
from matplotlib import pyplot as plt
from matplotlib import dates as mpDates
from .forms import queryForm

# Create your views here.
def index_view(request):
	# Use context to pass in data to webpage
	context = {}
	return render(request, 'data/index.html', context=context)

def future_view(request):
	context = {}

	
	# Do this after the user enters in data
	if(request.POST):
		form = queryForm(request.POST)
		if form.is_valid() == False:
			context['query_form'] = queryForm()
			return render(request, 'data/future.html', context=context)

		region = form.cleaned_data['region']
		houseType = form.cleaned_data['houseType']
		startDate = form.cleaned_data['startDate']
		endDate = form.cleaned_data['endDate']
		# print(region,houseType,startDate,endDate)
		with connection.cursor() as cursor:
			# Get House ID
			cursor.execute("SELECT id FROM data_house WHERE region = '{}' AND HouseType = '{}'".format(region, houseType))
			HouseId = cursor.fetchone()[0]

			context['region'] = region 
			context['type'] = houseType
			# Get listings
			cursor.execute("""
			SELECT Price, listingDate FROM data_price WHERE 
			houseId_id = '{}' 
			AND ( listingDate >= '{}' AND listingDate <= '{}')
			ORDER BY listingDate DESC
			""".format(HouseId, startDate, endDate))
			query = cursor.fetchall()
			data = []
			for item in query:
				info = {
					# 'price' : item[0],
					'price': f"{item[0]:,d}",
					'date' : item[1]
				}
				data.append(info)
			context['data'] = data

	else:
		form = queryForm()
		context['query_form'] = form



	return render(request, 'data/future.html', context=context)

def current_view(request):
	context = {}
	return render(request, 'data/current.html', context=context)

def create_plot(request):
	context = {}
	cursor = connection.cursor()
	region = 'Tallahassee Metro'
	houseType = 'Studio'
	cursor.execute("SELECT id FROM data_house WHERE region = '{}' AND HouseType = '{}'".format(region, houseType))
	id = cursor.fetchone()[0]


	cursor.execute("SELECT Price, listingDate FROM data_price WHERE houseId_id = '{}' ".format(id))
	data = cursor.fetchall()
	
	dates = []
	prices =[]

	for price in data:
		prices.append(price[0])
		dates.append( price[1])

	plt.plot(dates, prices)
	plt.title(region)
	plt.xlabel('Years')
	plt.savefig('plot/plot.png')

	return render(request, 'data/current.html', context=context)