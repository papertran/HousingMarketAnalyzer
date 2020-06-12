from django.shortcuts import render

# Create your views here.
def index_view(request):
	# Use context to pass in data to webpage
	context = {}
	return render(request, 'data/index.html', context=context)