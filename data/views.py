from django.shortcuts import render

# Create your views here.
def index_view(request):
	# Use context to pass in data to webpage
	context = {}
	return render(request, 'data/index.html', context=context)

def future_view(request):
	context = {}
	return render(request, 'data/future.html', context=context)

def current_view(request):
	context = {}
	return render(request, 'data/current.html', context=context)