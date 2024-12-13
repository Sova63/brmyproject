from django.shortcuts import render


def index(request):
	return render(request,'myapp/index.html')

def newsfirst(request):
	return render(request, 'myapp/newsfirst.html')
