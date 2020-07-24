from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib import pyplot as plt
from matplotlib import dates as mpDates
from .forms import queryForm

# Create your views here.
def index_view(request):
	# Use context to pass in data to webpage
	context = {}
	return render(request, 'data/index.html', context=context)

# Helper Function
# if true save graph
def create_plot(region, houseType, startDate, endDate, plotFuture = False):
	saveLocation = 'static/data/plot.png'
	if plotFuture:
		saveLocation = 'static/data/future.png'

	plt.cla()
	context = {}
	cursor = connection.cursor()
	# region = 'Tallahassee Metro'
	# houseType = 'Studio'
	cursor.execute("SELECT id FROM data_house WHERE region = '{}' AND HouseType = '{}'".format(region, houseType))
	id = cursor.fetchone()[0]


	# cursor.execute("SELECT Price, listingDate FROM data_price WHERE houseId_id = '{}' ".format(id))
	if plotFuture:
		cursor.execute("""
		SELECT Price, listingDate FROM data_price WHERE 
		houseId_id = '{}' 
		AND Predicted = True
		""".format(id))
	else:
		cursor.execute("""
		SELECT Price, listingDate FROM data_price WHERE 
		houseId_id = '{}' 
		AND ( listingDate >= '{}' AND listingDate <= '{}')
		""".format(id, startDate, endDate))

	
	data = cursor.fetchall()
	
	dates = []
	prices = []

	for price in data:
		# print(price)
		prices.append(price[0])
		dates.append( price[1])

	plt.plot(dates, prices)
	plt.title(region)
	plt.xlabel('Years')
	plt.savefig(saveLocation)


def current_view(request):
	context = {}

	# Do this after the user enters in data
	if(request.POST):
		form = queryForm(request.POST)
		if form.is_valid() == False:
			context['query_form'] = queryForm()
			return render(request, 'data/current.html', context=context)

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
			context['plot_exists'] = True
			create_plot(region, houseType, startDate, endDate)
			create_plot(region, houseType, startDate, endDate, True)




	else:
		form = queryForm()
		context['query_form'] = form
		context['plot_exists'] = False

	return render(request, 'data/current.html', context=context)


def show_plot(request):
	image_data = open("static/data/plot.png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")

def show_future_plot(request):
	image_data = open("static/data/future.png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")


def future_view(request):
	context = {}
	return render(request, 'data/future.html')