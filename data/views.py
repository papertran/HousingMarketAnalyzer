from django.shortcuts import render
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
		form = queryForm()
		context['query_form'] = form
	else:
		form = queryForm()
		context['query_form'] = form


	return render(request, 'data/future.html', context=context)

def current_view(request):
	context = {}
	return render(request, 'data/current.html', context=context)