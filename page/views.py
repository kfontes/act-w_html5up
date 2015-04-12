from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {'name': 'Kellie'}
	return render(request, "index.html", context_dict)
